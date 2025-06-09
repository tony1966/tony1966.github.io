# st-map-test-3.py
import streamlit as st
import pandas as pd

data=pd.DataFrame({
    'lat': [25.033968, 25.102398],
    'lon': [121.564468, 121.548492],
    '顏色' : ['#0000ff', [0, 255, 0]],
    '大小' : [100, 150]   
    })
st.map(data, latitude='lat', longitude='lon', size='大小', color='顏色')


