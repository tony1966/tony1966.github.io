# st-map-test-1.py
import streamlit as st
import pandas as pd

data=pd.DataFrame({
    'lat': [25.033968, 25.102398],
    'lon': [121.564468, 121.548492]
    })
st.map(data)


