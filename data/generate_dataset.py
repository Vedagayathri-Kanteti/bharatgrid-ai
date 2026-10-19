import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def calculate_apparent_temperature(temp_c, humidity_percent):
    """
    Computes Australian Bureau of Meteorology Apparent Temperature (Heat Index / Feels Like)
    Accurate and stable across 0C to 55C.
    """
    # Water vapor pressure (hPa)
    e = (humidity_percent / 100.0) * 6.105 * np.exp((17.27 * temp_c) / (237.7 + temp_c))
    # Apparent temperature formula (assuming mild breeze 2.5 m/s)
    at_c = temp_c + 0.33 * e - 0.70 * 2.5 - 4.0
    return float(np.clip(at_c, temp_c - 5.0, temp_c + 12.0))

def generate_grid_weather_dataset(start_date="2024-01-01", days=730, output_path="data/grid_weather_data.csv"):
    """
    Generates realistic hourly weather and electricity demand data for an urban metropolis.
    Incorporates seasonal heat waves, winter heating, and non-linear AC surge curves.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    np.random.seed(42)
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    total_hours = days * 24
    
    date_range = [start_dt + timedelta(hours=i) for i in range(total_hours)]
    
    data = []
    
    for dt in date_range:
        day_of_year = dt.timetuple().tm_yday
        hour = dt.hour
        day_of_week = dt.weekday()
        is_weekend = 1 if day_of_week >= 5 else 0
        month = dt.month
        
        # 1. Base Seasonal Temperature (Peak summer May-July ~38-44 C, Mild winter Dec-Jan ~12-20 C)
        annual_cycle = np.sin((day_of_year - 80) / 365.25 * 2 * np.pi)
        base_seasonal_temp = 27.0 + 12.0 * annual_cycle  # Range ~ 15C (winter) to 39C (summer)
        
        # Diurnal (Daily) Temperature cycle: minimum at 5 AM, maximum at 3 PM (hour 15)
        diurnal_temp = 5.0 * np.sin((hour - 9) / 24 * 2 * np.pi)
        
        # Weather noise & heatwave events
        weather_noise = np.random.normal(0, 1.2)
        heatwave_boost = 0.0
        if month in [5, 6] and (day_of_year % 18 < 3):
            heatwave_boost = np.random.uniform(2.0, 4.5)
            
        temperature_c = round(float(np.clip(base_seasonal_temp + diurnal_temp + weather_noise + heatwave_boost, 8.0, 46.0)), 1)
        
        # 2. Humidity: Lower on hottest summer afternoons, higher in monsoon/mornings
        monsoon_boost = 20.0 if month in [7, 8, 9] else 0.0
        diurnal_humidity = -12.0 * np.sin((hour - 9) / 24 * 2 * np.pi)
        humidity = round(float(np.clip(42.0 + diurnal_humidity + monsoon_boost + np.random.normal(0, 4.0), 18.0, 92.0)), 1)
        
        # 3. Heat Index / Apparent Temp
        heat_index_c = round(float(calculate_apparent_temperature(temperature_c, humidity)), 1)
        
        # 4. Solar Radiation (W/m^2): peaks at 12-1 PM, 0 at night
        if 6 <= hour <= 18:
            solar_irradiance = max(0.0, 950.0 * np.sin((hour - 6) / 12 * np.pi) * (1 - (humidity/220.0)) + np.random.normal(0, 25))
        else:
            solar_irradiance = 0.0
        solar_irradiance = round(float(np.clip(solar_irradiance, 0, 1050)), 1)
        
        # 5. Electricity Grid Demand (in Megawatts - MW)
        # Base Urban Load: lighting, hospitals, water pumping, server farms (~2000 MW)
        base_load = 2000.0
        
        # Commercial & Industrial Diurnal profile (Peaks 10 AM to 6 PM, drops on weekends)
        commercial_factor = 1.0 - (0.20 if is_weekend else 0.0)
        hour_profile = 0.5 + 0.5 * np.exp(-((hour - 14)**2) / 36.0)
        business_load = 850.0 * hour_profile * commercial_factor
        
        # AC / Cooling Surge (Hockey-stick surge above 27 C ambient)
        cooling_load = 0.0
        if temperature_c > 26.5:
            cdd = temperature_c - 26.5
            cooling_load = 110.0 * (cdd ** 1.18)
            # Humidity amplifies AC strain
            if humidity > 55.0:
                cooling_load *= (1.0 + (humidity - 55.0) * 0.005)
                
        # Winter heating load (Below 16 C in mornings/evenings)
        heating_load = 0.0
        if temperature_c < 18.0:
            hdd = 18.0 - temperature_c
            heating_load = 55.0 * (hdd ** 1.1) * (1.2 if hour in [6, 7, 8, 20, 21] else 0.7)
            
        load_noise = np.random.normal(0, 35)
        
        total_demand_mw = round(float(base_load + business_load + cooling_load + heating_load + load_noise), 1)
        grid_safe_capacity = 4200.0 # Metro grid transformer thermal safety line
        
        data.append({
            "timestamp": dt.strftime("%Y-%m-%d %H:%M:%S"),
            "hour": hour,
            "month": month,
            "day_of_week": day_of_week,
            "is_weekend": is_weekend,
            "temperature_c": temperature_c,
            "humidity_percent": humidity,
            "heat_index_c": heat_index_c,
            "solar_irradiance_wm2": solar_irradiance,
            "grid_demand_mw": total_demand_mw,
            "grid_safe_capacity_mw": grid_safe_capacity
        })
        
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {len(df)} records saved to {output_path}")
    print(f"Demand Range: {df['grid_demand_mw'].min()} MW to {df['grid_demand_mw'].max()} MW")
    print(f"Max Temp: {df['temperature_c'].max()} C, Max Apparent Temp: {df['heat_index_c'].max()} C")
    return output_path

if __name__ == "__main__":
    generate_grid_weather_dataset()
