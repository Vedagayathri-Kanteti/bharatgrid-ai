import pandas as pd
import numpy as np

class ClimatePowerScheduler:
    """
    Climate-Adaptive Electricity Allocation & Curtailment Engine.
    
    Core Philosophy:
    - Scorching / Extreme Sun: 100% UNINTERRUPTED POWER (People need cooling, fans, hydration).
    - Cool / Chilly / Breezy / Rainy: SAFE POWER CUT (People utilize natural comfort/ventilation).
    - Calculates exact Watts/Kilowatts/Megawatts saved by cutting power during pleasant weather,
      and routes that conserved power to hot zones that urgently need it.
    """
    def __init__(
        self,
        pleasant_temp_low=16.0,
        pleasant_temp_high=25.0,
        scorching_temp_threshold=33.0,
        base_zone_load_mw=120.0,
        cooling_load_per_degree_mw=8.5
    ):
        self.pleasant_low = pleasant_temp_low
        self.pleasant_high = pleasant_temp_high
        self.scorching_threshold = scorching_temp_threshold
        self.base_zone_load_mw = base_zone_load_mw
        self.cooling_load_per_degree_mw = cooling_load_per_degree_mw

    def evaluate_climate_comfort(self, temp_c, solar_wm2, wind_speed_kmh=10.0, humidity_percent=50.0):
        """
        Determines Natural Climate Comfort level:
        - 'SCORCHING_HOT': Sun is blazing, temp is high. People desperately need power. NEVER CUT.
        - 'MODERATE': Standard conditions. Regular power supply.
        - 'NATURAL_COMFORT': Cool, breezy, or cloudy. People can use open windows/breeze. SAFE TO CUT.
        """
        # Perceived warmth considering sun radiation and wind chill
        solar_warming = (solar_wm2 / 1000.0) * 3.0  # direct sun adds up to 3C of thermal sensation
        wind_cooling = (wind_speed_kmh / 20.0) * 2.0 # breeze cools perceived sensation
        perceived_temp = temp_c + solar_warming - wind_cooling
        
        if perceived_temp >= self.scorching_threshold or (temp_c >= 35.0):
            status = "SCORCHING_HOT"
            action = "CRITICAL_SUPPLY"
            cut_allowed = False
            curtailment_percent = 0.0
            reason = "High heat & blazing sun! Cooling & fans are critical. ZERO power cuts allowed."
        elif self.pleasant_low <= perceived_temp <= self.pleasant_high or (temp_c < self.pleasant_low + 2.0 and solar_wm2 < 300):
            status = "COOL_PLEASANT"
            action = "SAFE_POWER_CUT"
            cut_allowed = True
            # In cool weather, non-essential residential AC/fan load is eliminated.
            # 60% of regional grid load can be safely curtailed while people enjoy the natural weather.
            curtailment_percent = 0.60
            reason = "Weather is cool and pleasant! People can rely on natural climate. Power can be safely cut/saved."
        elif perceived_temp < self.pleasant_low:
            status = "CHILLY"
            action = "SAFE_POWER_CUT"
            cut_allowed = True
            curtailment_percent = 0.50
            reason = "Chilly weather. No cooling needed. Safe window to cut power and conserve energy."
        else:
            status = "MODERATE"
            action = "NORMAL_SUPPLY"
            cut_allowed = False
            curtailment_percent = 0.0
            reason = "Normal weather. Maintain standard power delivery."
            
        return {
            "perceived_temp_c": round(perceived_temp, 1),
            "climate_status": status,
            "department_action": action,
            "can_cut_power": cut_allowed,
            "curtailment_percent": curtailment_percent,
            "operational_reason": reason
        }

    def generate_zone_schedule(self, weather_df, zone_name="Metropolitan District"):
        """
        Processes a weather forecast timeline and builds the hour-by-hour
        Electricity Department Action Plan:
        - When to cut power (in cool hours)
        - When to supply 100% current (in hot sunny hours)
        - Exact Megawatts (MW) and Kilowatt-hours (kWh) saved
        """
        df = weather_df.copy()
        
        status_list = []
        action_list = []
        can_cut_list = []
        power_supplied_mw = []
        power_saved_mw = []
        reasons_list = []
        perceived_temps = []
        
        for idx, row in df.iterrows():
            temp = row["temperature_c"]
            solar = row.get("solar_irradiance_wm2", 500.0)
            wind = row.get("wind_speed_kmh", 12.0)
            humidity = row.get("humidity_percent", 50.0)
            
            eval_res = self.evaluate_climate_comfort(temp, solar, wind, humidity)
            
            # Baseline power demand for this area
            normal_demand = self.base_zone_load_mw
            if temp > 26.0:
                normal_demand += (temp - 26.0) * self.cooling_load_per_degree_mw
                
            curtail_pct = eval_res["curtailment_percent"]
            saved_mw = normal_demand * curtail_pct
            supplied_mw = normal_demand - saved_mw
            
            status_list.append(eval_res["climate_status"])
            action_list.append(eval_res["department_action"])
            can_cut_list.append(eval_res["can_cut_power"])
            power_supplied_mw.append(round(supplied_mw, 1))
            power_saved_mw.append(round(saved_mw, 1))
            reasons_list.append(eval_res["operational_reason"])
            perceived_temps.append(eval_res["perceived_temp_c"])
            
        df["perceived_temp_c"] = perceived_temps
        df["climate_status"] = status_list
        df["department_action"] = action_list
        df["can_cut_power"] = can_cut_list
        df["power_supplied_mw"] = power_supplied_mw
        df["power_saved_mw"] = power_saved_mw
        df["operational_reason"] = reasons_list
        
        # Aggregate totals
        total_mw_saved = sum(power_saved_mw)
        total_kwh_saved = total_mw_saved * 1000.0 # 1 MW for 1 hour = 1000 kWh
        total_watts_saved = total_kwh_saved * 1000.0 # in Watts
        total_cut_hours = sum([1 for c in can_cut_list if c])
        total_hot_hours = sum([1 for s in status_list if s == "SCORCHING_HOT"])
        
        summary = {
            "zone_name": zone_name,
            "total_cut_hours": total_cut_hours,
            "total_hot_hours": total_hot_hours,
            "total_mw_saved": round(total_mw_saved, 1),
            "total_kwh_saved": round(total_kwh_saved, 0),
            "total_watts_saved": round(total_watts_saved, 0),
            "avg_hourly_saving_mw": round(np.mean(power_saved_mw), 1)
        }
        
        return df, summary

    def multi_zone_balancer(self, zone_forecasts):
        """
        Simulates multiple areas of a state or city:
        - Cool areas have power safely cut.
        - The power saved from cool areas is directly diverted to burning hot areas!
        """
        zone_results = {}
        total_surplus_saved_mw = 0.0
        
        for zone_name, df in zone_forecasts.items():
            processed_df, summary = self.generate_zone_schedule(df, zone_name)
            zone_results[zone_name] = {
                "df": processed_df,
                "summary": summary
            }
            total_surplus_saved_mw += summary["total_mw_saved"]
            
        return zone_results, round(total_surplus_saved_mw, 1)
