# 🚴‍♂️ Ride Demand Prediction Dashboard

## 📌 Project Overview

This project predicts ride demand using machine learning based on factors such as traffic, weather, time, and driver availability.

An interactive dashboard is built using **Streamlit**, allowing users to explore data, visualize trends, and make real-time predictions.

---

## ⚙️ Features

* 📊 Data Overview (dataset preview & statistics)
* 📈 Data Visualization (distribution & hourly demand)
* 🤖 Machine Learning Model (Linear Regression)
* 🎯 Real-time Demand Prediction (interactive inputs)

---

## 🧠 Model Details

* Algorithm: Linear Regression
* Target Variable: `requests`
* Key Features:

  * Available Drivers
  * Rain (mm)
  * Traffic Index
  * Event Intensity
  * Hour

---

## 📊 Results

* R2 Score: ~0.52
* MAE: ~6.7

The model shows moderate prediction capability and provides useful demand estimates.

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live Demo

(Will be added after deployment)

---

## 📁 Project Structure

```
app.py
requirements.txt
fact_zone_hour.csv
dim_weather_hour.csv
dim_zone.csv
dim_holidays_tel.csv
README.md
```

---

## 🔮 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Improve feature engineering
* Add real-time data integration

---

## 👨‍💻 Author

SHAIK WAHEED
