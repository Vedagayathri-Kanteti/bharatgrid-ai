import requests
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from engine.india_grid_data import (
    INDIAN_GRID_DATA,
    get_indian_states,
    get_districts_for_state,
    get_villages_for_district,
    get_village_meta
)

def get_village_weather_forecast(state_name="Telangana", district_name="Hyderabad", village_name="Charminar Old City Feeder", forecast_hours=48):
    """
    Fetches real-time hourly satellite weather (Temperature, Sunshine, Cloud cover, Wind speed)
    from Open-Meteo free API for the specific Indian village / substation feeder.
    """
    meta = get_village_meta(state_name, district_name, village_name)
    lat = meta["lat"]
    lon = meta["lon"]
    
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,relative_humidity_2m,cloud_cover,wind_speed_10m,shortwave_radiation"
        f"&timezone=Asia/Kolkata&forecast_days=3"
    )
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            hourly = data.get("hourly", {})
            times = hourly.get("time", [])[:forecast_hours]
            temps = hourly.get("temperature_2m", [])[:forecast_hours]
            humidity = hourly.get("relative_humidity_2m", [])[:forecast_hours]
            cloud = hourly.get("cloud_cover", [])[:forecast_hours]
            winds = hourly.get("wind_speed_10m", [])[:forecast_hours]
            solar = hourly.get("shortwave_radiation", [])[:forecast_hours]
            
            df = pd.DataFrame({
                "timestamp": [datetime.fromisoformat(t) for t in times],
                "temperature_c": temps,
                "humidity_percent": humidity,
                "cloud_cover_percent": cloud,
                "wind_speed_kmh": winds,
                "solar_irradiance_wm2": solar
            })
            df["hour"] = df["timestamp"].dt.hour
            df["day_name"] = df["timestamp"].dt.strftime("%A")
            return df, "Live IMD / Open-Meteo Satellite Feed"
    except Exception as e:
        print(f"Weather API fallback for {village_name} ({e}). Using physical climate simulation...")
        
    return _generate_fallback_village_climate(meta, forecast_hours), "Calibrated Indian Physical Climate Simulation"

def _generate_fallback_village_climate(meta, forecast_hours=48):
    """
    Generates realistic diurnal physical weather for the specific Indian village / feeder.
    """
    now = datetime.now()
    climate_desc = meta.get("climate", "")
    
    if "Extreme" in climate_desc or "Scorching" in climate_desc or "Desert" in climate_desc or "Vidarbha" in climate_desc:
        base_temp = 41.0 # high heat summer (Phalodi, Nagpur, Ramagundam)
    elif "Mountain" in climate_desc or "Alpine" in climate_desc or "Highland" in climate_desc or "Cold" in climate_desc:
        base_temp = 18.0 # cool mountain climate (Shimla, Manali, Wayanad)
    elif "Coastal" in climate_desc or "Sea Breeze" in climate_desc:
        base_temp = 32.0 # humid coastal (Mumbai, Chennai, Bheemili)
    elif "Pleasant" in climate_desc:
        base_temp = 25.0 # Bengaluru, Mysore
    else:
        base_temp = 35.0 # standard Deccan / Gangetic summer plain
        
    records = []
    for i in range(forecast_hours):
        dt = now + timedelta(hours=i)
        hour = dt.hour
        
        # Diurnal temperature cycle: peak at 14:00 - 15:00, trough at 05:00
        diurnal = 6.5 * np.sin((hour - 9) / 24 * 2 * np.pi)
        temp = round(float(base_temp + diurnal + np.random.normal(0, 0.4)), 1)
        
        if 6 <= hour <= 18:
            solar = max(0.0, 960.0 * np.sin((hour - 6) / 12 * np.pi) + np.random.normal(0, 20))
        else:
            solar = 0.0
            
        wind = round(float(np.clip(12.0 + 4.0 * np.sin((hour - 14) / 24 * 2 * np.pi) + np.random.normal(0, 2), 3.0, 35.0)), 1)
        cloud = round(float(np.clip(30.0 + np.random.normal(0, 15), 0, 100)), 0)
        humidity = round(float(np.clip(55.0 - (temp - 25.0) * 1.5, 20.0, 85.0)), 1)
        
        records.append({
            "timestamp": dt,
            "temperature_c": temp,
            "humidity_percent": humidity,
            "cloud_cover_percent": cloud,
            "wind_speed_kmh": wind,
            "solar_irradiance_wm2": round(float(solar), 1),
            "hour": hour,
            "day_name": dt.strftime("%A")
        })
        
    return pd.DataFrame(records)

def get_state_all_villages_forecast(state_name="Telangana", forecast_hours=48):
    """
    Fetches forecasts for representative feeders across all districts of the selected state
    to enable intra-state DISCOM power balancing.
    """
    state_dict = INDIAN_GRID_DATA.get(state_name, INDIAN_GRID_DATA["Telangana"])
    districts = state_dict["districts"]
    
    all_data = {}
    for d_name, villages in districts.items():
        # Pick the first representative village/feeder in each district
        v_name = list(villages.keys())[0]
        df, _ = get_village_weather_forecast(state_name, d_name, v_name, forecast_hours)
        all_data[f"{d_name} ({v_name})"] = df
    return all_data

# Backwards compatibility aliases
get_zone_weather_forecast = lambda zone_name="Telangana", country_name="India", forecast_hours=48: get_village_weather_forecast(state_name="Telangana", forecast_hours=forecast_hours)
get_all_states_forecast = lambda country_name="India", forecast_hours=48: get_state_all_villages_forecast(state_name="Telangana", forecast_hours=forecast_hours)
get_countries = lambda: ["India"]
get_states_for_country = lambda country="India": get_indian_states()
COUNTRY_STATE_REGIONS = {"India": {s: {"lat": 20.5937, "lon": 78.9629, "climate_type": "Indian Subcontinent Grid", "base_load_mw": 100} for s in get_indian_states()}}
