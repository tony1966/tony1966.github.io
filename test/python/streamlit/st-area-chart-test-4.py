# st-area-chart-test-2.py
import streamlit as st
import pandas as pd

# 模擬每月營收資料
data=pd.DataFrame({
    '月份': ['1月', '2月', '3月', '4月', '5月'],
    '營收': [120000, 135000, 95000, 150000, 170000]
    })
st.subheader('今年前五月月營收區域圖')
st.area_chart(
    data,
    x='月份',
    y='營收',
    color='#FF6B6B',
    x_label='2025 年前五月',
    y_label='營收 (單位: 元)'
    )



