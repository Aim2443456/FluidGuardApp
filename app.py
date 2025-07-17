# Fluid Guard - AI Pipeline Health Predictor
import streamlit as st
import pandas as pd
import datetime
import numpy as np

st.set_page_config(page_title="Fluid Guard AI", layout="centered")
st.title("🛢️ Fluid Guard - Smart Pipeline Health Advisor")
st.write("Predict corrosion risk and maintenance schedules based on pipeline & fluid data.")

# --- User Inputs ---
st.header("1️⃣ Fluid & Pipeline Details")
fluid = st.selectbox("Fluid Type", ["Water", "Crude Oil", "Petrol", "Diesel", "Kerosene", "Other"])
temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=150.0, step=1.0)
density = st.number_input("Fluid Density (kg/m³)", min_value=500.0, max_value=1500.0, step=10.0)
humidity = st.slider("Humidity Level (%)", 0, 100, 60)

material = st.selectbox("Pipeline Material", ["Iron", "Aluminium", "Copper", "Duralumin", "Composite"])
install_date = st.date_input("Pipeline Installation Date", value=datetime.date(2018, 1, 1))
flow_freq = st.slider("Flow Frequency (hours/day)", 0, 24, 12)
maint_interval = st.slider("Maintenance Interval (days)", 30, 365, 180)

# --- Prediction Logic (Mock ML with rules) ---


today = datetime.date.today()
days_since_install = (today - install_date).days

# Simulate risk score (this would be replaced by a trained model)
risk_score = (
    (1 if material in ["Iron", "Duralumin"] else 0.7) +
    (density / 1000) +
    (temp / 100) +
    (humidity / 100) +
    (flow_freq / 24) -
    (maint_interval / 365)
)
risk_score = np.clip(risk_score, 0, 3)

# Estimate corrosion and replacement timing
corrosion_days = int(1000 / risk_score)
replacement_days = int(2500 / risk_score)
corrosion_date = install_date + datetime.timedelta(days=corrosion_days)
replacement_date = install_date + datetime.timedelta(days=replacement_days)

# Maintenance advice
maint_ok = (maint_interval < (corrosion_days // 4))

st.header("2️⃣ Prediction Results")
st.write(f"🔶 **Estimated Corrosion Starts:** {corrosion_date.strftime('%B %Y')}")
st.write(f"🔴 **Recommended Pipeline Replacement:** {replacement_date.strftime('%B %Y')}")
if maint_ok:
    st.success("✅ Your maintenance schedule is adequate.")
else:
    st.warning("⚠️ Maintenance interval too long. Consider reducing to avoid early rust.")


# --- Suggestions ---
st.header("💡 Suggestions")

if not maint_ok:
    suggested_interval = max(30, corrosion_days // 5)
    st.info(f"📉 Suggested Maintenance Interval: Every {suggested_interval} days")

if flow_freq > 16:
    st.warning("📛 High flow frequency detected. Consider reducing to minimize wear and corrosion risk.")
elif flow_freq < 6:
    st.info("🔁 Low flow frequency. This is generally safer, but verify fluid stagnation is not a risk.")
else:
    st.success("✅ Flow frequency is within a safe operating range.")

st.markdown("---")
st.caption("Fluid Guard - Built for predictive pipeline care in Nigeria and beyond. 🚀")
