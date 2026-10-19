import pandas as pd
import numpy as np

class SmartGridOptimizer:
    """
    Intelligent Energy Storage & Peak-Shaving Dispatch Engine.
    Manages Battery Energy Storage Systems (BESS) and priority-based
    load balancing to eliminate harsh peak-heat power cuts.
    """
    def __init__(
        self,
        battery_capacity_mwh=1200.0,
        initial_soc_percent=75.0,
        max_charge_mw=300.0,
        max_discharge_mw=500.0,
        roundtrip_efficiency=0.92,
        min_soc_percent=10.0,
        max_soc_percent=95.0,
        grid_safe_capacity_mw=4200.0
    ):
        self.capacity_mwh = battery_capacity_mwh
        self.initial_soc = initial_soc_percent
        self.max_charge_mw = max_charge_mw
        self.max_discharge_mw = max_discharge_mw
        self.efficiency = roundtrip_efficiency
        self.min_soc = min_soc_percent
        self.max_soc = max_soc_percent
        self.safe_capacity = grid_safe_capacity_mw

    def run_dispatch_simulation(self, forecast_df):
        """
        Simulates hour-by-hour storage charge/discharge and load balancing
        over the forecasted timeline.
        """
        df = forecast_df.copy()
        
        current_stored_mwh = (self.initial_soc / 100.0) * self.capacity_mwh
        min_allowed_mwh = (self.min_soc / 100.0) * self.capacity_mwh
        max_allowed_mwh = (self.max_soc / 100.0) * self.capacity_mwh
        
        battery_action = []        # 'CHARGING', 'DISCHARGING', 'IDLE'
        battery_flow_mw = []       # + for discharge (supplying grid), - for charge (storing)
        battery_soc_percent = []
        stored_energy_mwh = []
        net_grid_load_mw = []
        grid_status = []           # 'STABLE', 'PEAK_DEFICIT_AVERTED', 'LOAD_SHIFT_BALANCED', etc.
        blackouts_avoided = []
        curtailed_industrial_mw = []
        
        for idx, row in df.iterrows():
            demand = row["predicted_demand_mw"]
            deficit = demand - self.safe_capacity
            
            flow = 0.0
            action = "IDLE"
            status = "STABLE"
            avoided = 0
            curtailed_ind = 0.0
            
            # CASE 1: Grid Overload / Peak Deficit (Mid-afternoon heat surge)
            if deficit > 0:
                available_to_discharge = max(0.0, (current_stored_mwh - min_allowed_mwh) * self.efficiency)
                needed_discharge = min(deficit, self.max_discharge_mw)
                
                actual_discharge = min(needed_discharge, available_to_discharge)
                
                if actual_discharge > 0:
                    flow = actual_discharge
                    action = "DISCHARGING"
                    current_stored_mwh -= (actual_discharge / self.efficiency)
                    current_stored_mwh = max(min_allowed_mwh, current_stored_mwh)
                    
                remaining_deficit = deficit - actual_discharge
                
                if remaining_deficit <= 5.0:
                    status = "PEAK_DEFICIT_AVERTED"
                    avoided = 1
                else:
                    # Battery alone cannot cover full deficit: Trigger industrial demand-response
                    # Stagger agricultural / non-critical industrial load
                    curtailed_ind = min(remaining_deficit, 400.0)
                    remaining_after_curtail = remaining_deficit - curtailed_ind
                    
                    if remaining_after_curtail <= 15.0:
                        status = "LOAD_SHIFT_BALANCED"
                        avoided = 1
                    else:
                        status = "HIGH_STRESS_ALERT"
                        avoided = 0
                        
            # CASE 2: Grid Surplus (Early morning, Solar peak, or Winter)
            elif deficit < -100.0:
                surplus = abs(deficit)
                capacity_to_store = max(0.0, max_allowed_mwh - current_stored_mwh)
                
                charge_rate = min(self.max_charge_mw, surplus * 0.5, capacity_to_store)
                
                if charge_rate > 5.0:
                    flow = -charge_rate # negative indicates charging
                    action = "CHARGING"
                    current_stored_mwh += (charge_rate * self.efficiency)
                    current_stored_mwh = min(max_allowed_mwh, current_stored_mwh)
                status = "SURPLUS_STORED"
            else:
                action = "IDLE"
                status = "NORMAL_BALANCED"
                
            soc = (current_stored_mwh / self.capacity_mwh) * 100.0
            net_load = demand - flow - curtailed_ind
            
            battery_action.append(action)
            battery_flow_mw.append(round(flow, 1))
            battery_soc_percent.append(round(soc, 1))
            stored_energy_mwh.append(round(current_stored_mwh, 1))
            net_grid_load_mw.append(round(net_load, 1))
            grid_status.append(status)
            blackouts_avoided.append(avoided)
            curtailed_industrial_mw.append(round(curtailed_ind, 1))
            
        df["battery_action"] = battery_action
        df["battery_flow_mw"] = battery_flow_mw
        df["battery_soc_percent"] = battery_soc_percent
        df["stored_energy_mwh"] = stored_energy_mwh
        df["net_grid_load_mw"] = net_grid_load_mw
        df["grid_status"] = grid_status
        df["blackout_avoided"] = blackouts_avoided
        df["curtailed_industrial_mw"] = curtailed_industrial_mw
        df["grid_safe_capacity_mw"] = self.safe_capacity
        
        # Summary Analytics
        total_discharged_mwh = sum([f for f in battery_flow_mw if f > 0])
        total_charged_mwh = sum([abs(f) for f in battery_flow_mw if f < 0])
        total_blackouts_averted_hours = sum(blackouts_avoided)
        co2_saved_tons = round(total_discharged_mwh * 0.85, 1) # ~0.85 tons CO2 per MWh vs coal/gas peakers
        
        summary = {
            "total_discharged_mwh": round(total_discharged_mwh, 1),
            "total_charged_mwh": round(total_charged_mwh, 1),
            "blackouts_averted_hours": total_blackouts_averted_hours,
            "co2_saved_tons": co2_saved_tons,
            "final_battery_soc": battery_soc_percent[-1] if battery_soc_percent else self.initial_soc
        }
        
        return df, summary
