# st-map-test-5.py
import streamlit as st
import pandas as pd
import numpy as np

st.subheader('高雄登革熱疫情模擬地圖')
# 輸入病例數
case_count=st.slider('模擬病例數量', min_value=10, max_value=500, value=100, step=10)
center_lat=22.6300  # 高雄市中心緯度
center_lon=120.3000  # 高雄市中心經度
theta=np.random.uniform(0, 2 * np.pi, case_count)  # 隨機角度 (0~2π)
r=np.random.uniform(0, 0.02, case_count) # 隨機半徑 (0 ~ r)，r=0.02
lat=center_lat + r * np.sin(theta) # 生成隨機病例位置緯度 (Numpy 陣列)
lon=center_lon + r * np.cos(theta) # 生成隨機病例位置經度 (Numpy 陣列)
data=pd.DataFrame({'lat': lat,'lon': lon})  # 建立 DataFrame
st.map(
    data,
    latitude='lat',
    longitude='lon',
    color='#FF0000',
    size=80,
    zoom=12
    )
