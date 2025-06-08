# st-area-chart-test-1.py
import streamlit as st
import pandas as pd

# 模擬每月營收資料
data=pd.DataFrame({
    '月份': ['一月', '二月', '三月', '四月', '五月'],
    '營收': [120000, 135000, 95000, 150000, 170000]
    })
st.subheader('今年前五月月營收區域圖')
st.area_chart(data=data, x='月份', y='營收')


