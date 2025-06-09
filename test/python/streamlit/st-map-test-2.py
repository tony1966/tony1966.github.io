# st-map-test-2.py
import streamlit as st
import pandas as pd

data=pd.DataFrame({
    'lat': [25.033968, 25.102398],
    'lon': [121.564468, 121.548492]
    })
st.map(data, latitude='lat', longitude='lon', size=100, color='#0000FF')


