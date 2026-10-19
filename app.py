import os
import importlib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Force reload local modules so changes on disk are immediately reflected
import engine.india_grid_data
importlib.reload(engine.india_grid_data)
import engine.weather_service
importlib.reload(engine.weather_service)
import engine.climate_scheduler
importlib.reload(engine.climate_scheduler)

from engine.india_grid_data import (
    get_indian_states,
    get_districts_for_state,
    get_villages_for_district,
    get_village_meta
)
from engine.weather_service import (
    get_village_weather_forecast,
    get_state_all_villages_forecast
)
from engine.climate_scheduler import ClimatePowerScheduler

st.set_page_config(
    page_title="BharatGrid | India Climate-Adaptive Electricity Management",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Indian DISCOM Command Center
st.markdown("""
<style>
    .main { background-color: #0b0f19; }
    .badge-hot {
        background-color: rgba(239, 68, 68, 0.2);
        color: #f87171;
        border: 1px solid #ef4444;
        padding: 4px 10px;
        border-radius: 16px;
        font-weight: 700;
        font-size: 0.82rem;
    }
    .badge-cool {
        background-color: rgba(16, 185, 129, 0.2);
        color: #34d399;
        border: 1px solid #10b981;
        padding: 4px 10px;
        border-radius: 16px;
        font-weight: 700;
        font-size: 0.82rem;
    }
    .badge-moderate {
        background-color: rgba(59, 130, 246, 0.2);
        color: #60a5fa;
        border: 1px solid #3b82f6;
        padding: 4px 10px;
        border-radius: 16px;
        font-weight: 700;
        font-size: 0.82rem;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR CONTROLS -----------------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/india.png", width=56)
    st.title("BharatGrid AI")
    st.caption("🇮🇳 Climate-Adaptive Electricity Management for India")
    st.markdown("---")
    
    st.subheader("Village & Substation Locator")
    all_states = get_indian_states()
    selected_state = st.selectbox("1. Select Indian State", all_states, index=all_states.index("Telangana") if "Telangana" in all_states else 0)
    
    districts = get_districts_for_state(selected_state)
    selected_district = st.selectbox("2. Select District", districts, index=0)
    
    villages = get_villages_for_district(selected_state, selected_district)
    selected_village = st.selectbox("3. Select Village / Substation Feeder", villages, index=0)
    
    # Metadata for the selected feeder
    v_meta = get_village_meta(selected_state, selected_district, selected_village)
    
    st.markdown("---")
    st.markdown(f"""
    **DISCOM:** `{v_meta['discom']}`  
    **Feeder Type:** `{v_meta['type']}`  
    **Climate Zone:** `{v_meta['climate']}`  
    **Feeder Base Load:** `{v_meta['base_load_mw']} MW`  
    """)
    
    horizon_hours = st.slider("Forecast Timeline (Hours)", min_value=24, max_value=72, value=48, step=12)
    
    st.markdown("---")
    st.subheader("Natural Comfort Rules (India)")
    st.caption("Thermal comfort thresholds for rural and urban Indian households.")
    pleasant_low = st.slider("Pleasant Weather Floor (°C)", 14.0, 22.0, 18.0, 0.5)
    pleasant_high = st.slider("Pleasant Weather Ceiling (°C)", 22.0, 28.0, 25.0, 0.5)
    scorching_limit = st.slider("Scorching Heat Cutoff (°C)", 30.0, 42.0, 34.0, 0.5)
    
    st.markdown("---")
    st.subheader("Weather Simulation Slider")
    st.info("Simulate summer heatwaves (Loo winds) or sudden rain showers.")
    sim_temp_offset = st.slider("Simulate Temp Shift (°C)", -6.0, 8.0, 0.0, 0.5)
    sim_sun_factor = st.slider("Simulate Sunshine Intensity", 0.3, 1.8, 1.0, 0.1)

# ----------------- DATA INGESTION & SCHEDULING -----------------
raw_df, data_source = get_village_weather_forecast(
    state_name=selected_state,
    district_name=selected_district,
    village_name=selected_village,
    forecast_hours=horizon_hours
)

# Apply simulation offsets
sim_df = raw_df.copy()
sim_df["temperature_c"] = np.clip(sim_df["temperature_c"] + sim_temp_offset, 3.0, 52.0)
sim_df["solar_irradiance_wm2"] = np.clip(sim_df["solar_irradiance_wm2"] * sim_sun_factor, 0.0, 1150.0)

# Run Climate Scheduler
scheduler = ClimatePowerScheduler(
    pleasant_temp_low=pleasant_low,
    pleasant_temp_high=pleasant_high,
    scorching_temp_threshold=scorching_limit,
    base_zone_load_mw=float(v_meta["base_load_mw"])
)
schedule_df, summary = scheduler.generate_zone_schedule(sim_df, zone_name=f"{selected_village}, {selected_district}")

# ----------------- HEADER & EXECUTIVE STATUS -----------------
col_head, col_badge = st.columns([3, 1])
with col_head:
    st.title(f"{selected_village}")
    st.markdown(f"**District:** `{selected_district}` &nbsp;|&nbsp; **State:** `{selected_state}` &nbsp;|&nbsp; **DISCOM:** `{v_meta['discom']}` &nbsp;|&nbsp; **Satellite Feed:** `{data_source}`")

with col_badge:
    current_status = schedule_df.iloc[0]["climate_status"]
    if current_status == "SCORCHING_HOT":
        st.markdown('<br><span class="badge-hot">MID-AFTERNOON HEAT: FULL POWER MANDATORY</span>', unsafe_allow_html=True)
    elif "COOL" in current_status or "CHILLY" in current_status:
        st.markdown('<br><span class="badge-cool">COOL BREEZE: SAFE POWER CUT ACTIVE</span>', unsafe_allow_html=True)
    else:
        st.markdown('<br><span class="badge-moderate">NORMAL WEATHER: STANDARD SUPPLY</span>', unsafe_allow_html=True)

# ----------------- KPI METRIC CARDS -----------------
st.markdown("### Operational Energy Summary")
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:
    st.metric(
        label="Total Watts Saved",
        value=f"{summary['total_watts_saved']:,.0f} W",
        delta="During Pleasant Hours",
        delta_color="normal"
    )

with kpi2:
    st.metric(
        label="Energy Conserved",
        value=f"{summary['total_kwh_saved']:,.0f} kWh",
        delta=f"{summary['total_mw_saved']:,.1f} MWh",
        delta_color="normal"
    )

with kpi3:
    st.metric(
        label="Safe Power Cut Windows",
        value=f"{summary['total_cut_hours']} Hours",
        delta="Natural Breeze Active",
        delta_color="normal"
    )

with kpi4:
    st.metric(
        label="Full Power Windows",
        value=f"{summary['total_hot_hours']} Hours",
        delta="Zero Cut Guarantee",
        delta_color="off"
    )

with kpi5:
    st.metric(
        label="Avg Power Saved / Hour",
        value=f"{summary['avg_hourly_saving_mw']:,.1f} MW",
        delta="Available to Redirect",
        delta_color="normal"
    )

st.markdown("---")

# ----------------- DASHBOARD TABS -----------------
tab_plan, tab_climate, tab_rerouting, tab_table = st.tabs([
    f"{selected_village} Feeder Schedule",
    "Climate & Solar Radiation Curve",
    f"State DISCOM Balancing ({selected_state})",
    "Hourly Feeder Log"
])

# TAB 1: Department Action Schedule
with tab_plan:
    st.subheader(f"DISCOM Feeder Strategy for {selected_village}")
    st.caption(f"When it is scorching hot outside, households receive 100% full-time current for fans and refrigeration. When it is cool and breezy, power is cut so citizens use natural ventilation, saving thousands of Watts.")
    
    fig_action = go.Figure()
    
    # Supplied Power Line
    fig_action.add_trace(go.Scatter(
        x=schedule_df["timestamp"],
        y=schedule_df["power_supplied_mw"],
        mode="lines",
        name=f"Current Released to Feeder (MW)",
        line=dict(color="#10b981", width=3),
        fill="tozeroy",
        fillcolor="rgba(16, 185, 129, 0.15)",
        hovertemplate="Power Supplied: %{y:.1f} MW<extra></extra>"
    ))
    
    # Saved Power Line (Curtailed during cool weather)
    fig_action.add_trace(go.Scatter(
        x=schedule_df["timestamp"],
        y=schedule_df["power_saved_mw"],
        mode="lines",
        name="Watts Conserved by Eco-Cuts (MW)",
        line=dict(color="#38bdf8", width=2.5, dash="dash"),
        fill="tozeroy",
        fillcolor="rgba(56, 189, 248, 0.15)",
        hovertemplate="Power Saved: %{y:.1f} MW<extra></extra>"
    ))
    
    fig_action.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        height=400,
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(title="Timeline (Day & Hour IST)", showgrid=True, gridcolor="#334155"),
        yaxis=dict(title="Megawatts (MW)", showgrid=True, gridcolor="#334155")
    )
    st.plotly_chart(fig_action, use_container_width=True)
    
    # Action Status Bar
    st.subheader("Hourly Feeder Action Decision Bar")
    action_colors = [
        "#ef4444" if act == "CRITICAL_SUPPLY" else ("#10b981" if act == "SAFE_POWER_CUT" else "#3b82f6")
        for act in schedule_df["department_action"]
    ]
    
    fig_bar = go.Figure(go.Bar(
        x=schedule_df["timestamp"],
        y=[1] * len(schedule_df),
        marker_color=action_colors,
        customdata=schedule_df[["climate_status", "operational_reason", "power_saved_mw"]],
        hovertemplate="<b>Status:</b> %{customdata[0]}<br><b>DISCOM Action:</b> %{customdata[1]}<br><b>Watts Saved:</b> %{customdata[2]} MW<extra></extra>"
    ))
    fig_bar.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        height=130,
        margin=dict(l=20, r=20, t=10, b=10),
        yaxis=dict(visible=False),
        xaxis=dict(title="Hover over time slices to see DISCOM action", showgrid=False)
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("""
    <div style="display: flex; gap: 20px; font-size: 0.85rem; margin-top: -10px;">
        <div><span style="color:#ef4444;">■</span> <b>Red:</b> Scorching Hot (Full Power - No Cuts in Village)</div>
        <div><span style="color:#10b981;">■</span> <b>Green:</b> Cool & Pleasant (Power Cut - Villagers use natural air, Energy Saved)</div>
        <div><span style="color:#3b82f6;">■</span> <b>Blue:</b> Normal Weather (Standard Power)</div>
    </div>
    """, unsafe_allow_html=True)

# TAB 2: Climate Estimation
with tab_climate:
    st.subheader(f"Hyper-Local Satellite Climate for {selected_village}")
    st.caption(f"Coordinates: Latitude {v_meta['lat']}, Longitude {v_meta['lon']} | Climate Zone: {v_meta['climate']}")
    
    fig_clim = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_clim.add_trace(go.Scatter(
        x=schedule_df["timestamp"],
        y=schedule_df["temperature_c"],
        name="Ambient Temperature (°C)",
        line=dict(color="#f43f5e", width=3)
    ), secondary_y=False)
    
    fig_clim.add_trace(go.Scatter(
        x=schedule_df["timestamp"],
        y=schedule_df["perceived_temp_c"],
        name="Perceived Thermal Sensation (°C)",
        line=dict(color="#fb923c", width=2, dash="dot")
    ), secondary_y=False)
    
    fig_clim.add_trace(go.Scatter(
        x=schedule_df["timestamp"],
        y=schedule_df["solar_irradiance_wm2"],
        name="Solar Sunshine (W/m²)",
        line=dict(color="#eab308", width=1.5),
        fill="tozeroy",
        fillcolor="rgba(234, 179, 8, 0.12)"
    ), secondary_y=True)
    
    # Pleasant temperature band shading
    fig_clim.add_hrect(
        y0=pleasant_low, y1=pleasant_high,
        fillcolor="rgba(16, 185, 129, 0.12)",
        line_width=0,
        annotation_text="Natural Comfort Zone (Safe to Cut)",
        annotation_position="top left",
        secondary_y=False
    )
    
    fig_clim.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        height=420,
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig_clim.update_yaxes(title_text="Temperature (°C)", secondary_y=False, showgrid=True, gridcolor="#334155")
    fig_clim.update_yaxes(title_text="Solar Sunshine (W/m²)", secondary_y=True, showgrid=False)
    st.plotly_chart(fig_clim, use_container_width=True)

# TAB 3: State-Wide Intra-DISCOM Balancing
with tab_rerouting:
    st.subheader(f"Intra-State Grid Balancing across Districts in {selected_state}")
    st.markdown(f"""
    State DISCOMs (`{v_meta['discom']}`) manage power across diverse rural and urban feeders. 
    Districts experiencing pleasant/cool weather safely cut power, allowing villagers and residents to enjoy natural breeze.
    The electricity saved is instantly diverted to scorching heatwave districts in {selected_state}.
    """)
    
    all_districts_weather = get_state_all_villages_forecast(state_name=selected_state, forecast_hours=horizon_hours)
    multi_results, total_diverted_mw = scheduler.multi_zone_balancer(all_districts_weather)
    
    st.success(f"**State Grid Energy Transfer:** Across {selected_state}, **{total_diverted_mw:,.1f} MWh** of electricity is conserved from cool/pleasant districts and ready to be diverted to scorching heatwave feeders.")
    
    district_cards = []
    for d_name, d_data in multi_results.items():
        d_df = d_data["df"]
        d_sum = d_data["summary"]
        max_temp = d_df["temperature_c"].max()
        avg_temp = d_df["temperature_c"].mean()
        
        if max_temp >= 35.0:
            grid_role = "RECEIVE POWER (Extreme Heatwave)"
        elif max_temp <= 26.0 or d_sum['total_cut_hours'] >= 18:
            grid_role = "DONATE POWER (Cool / Safe to Cut)"
        else:
            grid_role = "BALANCED (Self-Sustaining)"
            
        district_cards.append({
            "District (Representative Feeder)": d_name,
            "Max Temp (°C)": f"{max_temp:.1f}°C",
            "Avg Temp (°C)": f"{avg_temp:.1f}°C",
            "Cool Cut Hours": f"{d_sum['total_cut_hours']} hrs",
            "Energy Saved (MWh)": f"{d_sum['total_mw_saved']:,.1f} MWh",
            "Watts Conserved": f"{d_sum['total_watts_saved']:,.0f} W",
            "State Grid Role": grid_role
        })
        
    st.table(pd.DataFrame(district_cards))
    
    st.subheader(f"Real-Time Inter-District Power Transfer Dynamics ({selected_state})")
    cool_dists = [row['District (Representative Feeder)'] for row in district_cards if "DONATE" in row['State Grid Role']]
    hot_dists = [row['District (Representative Feeder)'] for row in district_cards if "RECEIVE" in row['State Grid Role']]
    
    col_donor, col_receiver = st.columns(2)
    with col_donor:
        st.markdown(f"""
        **Power Donating Districts (Cool Climate / Cuts Active):**
        * {', '.join(cool_dists[:3]) if cool_dists else 'Currently all districts hot'}
        * **Citizen Impact:** Citizens open windows and use natural evening/morning breezes.
        * **Output:** Feeder power is disconnected to conserve megawatts.
        """)
    with col_receiver:
        st.markdown(f"""
        **Power Receiving Districts (Scorching Heat / Full Current):**
        * {', '.join(hot_dists[:3]) if hot_dists else 'All districts within safe thermal limits'}
        * **Citizen Impact:** Fans, water coolers, and refrigerators stay 100% on.
        * **Output:** Zero mid-afternoon power cuts during peak heat.
        """)

# TAB 4: Detailed Hourly Feeder Log
with tab_table:
    st.subheader(f"Hourly Dispatch Timetable for {selected_village}")
    st.caption(f"Hour-by-hour operational log for {v_meta['discom']} substation assistant engineers.")
    
    display_table = schedule_df[[
        "timestamp", "day_name", "temperature_c", "solar_irradiance_wm2", 
        "climate_status", "department_action", "power_saved_mw", "operational_reason"
    ]].copy()
    
    display_table["Watts Saved"] = (display_table["power_saved_mw"] * 1000.0 * 1000.0).apply(lambda x: f"{x:,.0f} W" if x > 0 else "0 W")
    display_table["Current Supplied"] = (schedule_df["power_supplied_mw"]).apply(lambda x: f"{x:,.1f} MW")
    
    display_table = display_table[[
        "timestamp", "day_name", "temperature_c", "solar_irradiance_wm2",
        "climate_status", "department_action", "Current Supplied", "Watts Saved", "operational_reason"
    ]]
    
    display_table.columns = [
        "Date & Time (IST)", "Day", "Temp (°C)", "Solar (W/m²)", 
        "Climate Status", "DISCOM Action", "Current Supplied", "Watts Saved", "Reason / Decision"
    ]
    
    st.dataframe(display_table, use_container_width=True)

# ----------------- FOOTER -----------------
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #64748b; font-size: 0.85rem;">
    <b>BharatGrid AI</b> • Climate-Adaptive Electricity Management for India<br>
    Monitoring {selected_village}, {selected_district}, {selected_state} | Under {v_meta['discom']} Jurisdiction.
</div>
""", unsafe_allow_html=True)
