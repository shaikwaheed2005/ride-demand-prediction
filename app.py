import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title = "Ride Demand Prediction", layout = "wide")

st.title("🚴‍♂️ Ride Demand Prediction Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("fact_zone_hour (1).csv")

data = load_data()

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Requests", int(data['requests'].mean()))
col2.metric("Max Requests", int(data['requests'].max()))
col3.metric("Min Requests", int(data['requests'].min()))

st.header("📊 Data Overview")

col1, col2 = st.columns(2)

with col1:
    st.write("Sample Data")
    st.dataframe(data.head())

with col2:
    st.write("Dataset Info")
    st.write(data.describe())

st.header("📈 Data Visualization")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Requests Distribution")
    fig, ax = plt.subplots()
    sns.histplot(data['requests'], bins = 50, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Demand by Hour")
    fig, ax=plt.subplots()
    sns.boxplot(x='hour', y='requests', data=data, ax=ax)
    st.pyplot(fig)

st.header("🤖 Predict Ride Demand")

features = [
    'available_drivers',
    'rain_mm',
    'traffic_index',
    'event_intensity_city',
    'hour'
]

TARGET = "requests"

model_df = data[features + [TARGET]].dropna()

x = model_df[features]
y = model_df[TARGET]

model = LinearRegression()
model.fit(x, y)

col1, col2 = st.columns(2)

with col1:
    available_drivers = st.number_input("Available Drivers", 0, 500, 100)
    rain_mm = st.number_input("Rain (mm)", 0.0, 100.0, 0.0)
    traffic_index = st.slider("Traffic Index", 0, 100, 50)

with col2:
    event_intensity_city = st.slider("Event Intensity", 0, 10, 1)
    hour = st.slider("Hour of Day", 0, 23, 12)

if st.button("Predict Demand"):
    input_data = np.array([[available_drivers, rain_mm, traffic_index, event_intensity_city, hour]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Ride Requests: {int(prediction[0])}")


st.markdown("---")
st.markdown("Built using Streamlit | ML Model: Linear Regression")
st.markdown("©️ Copyrights @ SHAIK WAHEED")