# app_streamlit.py
import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import json
import os

MODEL_PATH = r"D:/Projects/Sales_TimeSeries_Forecasting/Models/sarima_model_v1.pkl"
META_PATH  = r"D:/Projects/Sales_TimeSeries_Forecasting/Models/sarima_meta_v1.json"

@st.cache_resource
def load_model_and_meta():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model not found: {MODEL_PATH}")
        st.stop()
    if not os.path.exists(META_PATH):
        st.error(f"Meta not found: {META_PATH}")
        st.stop()
    with open(META_PATH,'r') as f:
        meta = json.load(f)
    sarima = sm.load(MODEL_PATH)
    return sarima, meta

st.title("Sales Forecast Demo (SARIMA)")
sarima, meta = load_model_and_meta()
st.write("Model:", meta.get("model_name","SARIMA"), "version:", meta.get("model_version"))

h = st.number_input("Forecast horizon (days)", min_value=1, max_value=365, value=30)
if st.button("Forecast"):
    with st.spinner("Generating forecast..."):
        fc = sarima.get_forecast(steps=int(h))
        mean = fc.predicted_mean
        ci = fc.conf_int()
        start_date = pd.to_datetime(meta["train_end"]) + pd.Timedelta(days=1)
        freq = meta.get("index_freq") or "D"
        try:
            idx = pd.date_range(start=start_date, periods=int(h), freq=freq)
        except Exception:
            idx = pd.date_range(start=start_date, periods=int(h), freq="D")
        df = pd.DataFrame({
            "date": idx,
            "forecast": mean.values,
            "lower": ci.iloc[:,0].values,
            "upper": ci.iloc[:,1].values
        })
        st.line_chart(df.set_index("date")[["forecast"]])
        st.dataframe(df.head(50))
        st.download_button("Download CSV", df.to_csv(index=False), file_name="sarima_forecast.csv")
