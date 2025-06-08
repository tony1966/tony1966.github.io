# st-scatter-chart-test-4.py
import streamlit as st
import pandas as pd
import numpy as np

# 建立隨機資料
np.random.seed(42)  # 確保數據可重現
data=pd.DataFrame({
    'x': np.random.randn(100),  # 隨機生成 100 個 x 座標
    'y': np.random.randn(100) * 2,  # 隨機生成 100 個 y 座標
    'size': np.random.rand(100) * 100,  # 隨機生成散點大小
    'category': np.random.choice(['A', 'B', 'C'], 100)  # 隨機分類
    })
st.subheader('隨機散布圖')
st.scatter_chart(
    data,
    x='x',
    y='y',
    size='size',  # 控制資料點大小
    color='category',  # 根據類別上色
    )
