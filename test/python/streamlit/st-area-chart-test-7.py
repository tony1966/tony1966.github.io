# st-area-chart-test-3.py
import streamlit as st
import pandas as pd

# 模擬每月營收資料
data=pd.DataFrame({
    '月份': ['1月', '2月', '3月', '4月', '5月'],
    '師大店營收': [120000, 135000, 95000, 150000, 170000],
    '內湖店營收': [90000, 102000, 99000, 130000, 160000]
    })
st.subheader('今年前五月月營收區域圖')
st.area_chart(
    data=data,
    x='月份',
    y=['師大店營收', '內湖店營收'],
    stack=True
    )




