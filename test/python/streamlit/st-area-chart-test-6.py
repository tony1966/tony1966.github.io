# st-area-chart-test-6.py
import streamlit as st
import pandas as pd

# 模擬每月營收資料
data=pd.DataFrame({
    '月份': ['一月', '二月', '三月', '四月', '五月'],
    '師大店營收': [120000, 135000, 95000, 150000, 170000],
    '內湖店營收': [90000, 102000, 99000, 130000, 160000]
    })
st.subheader('今年前五月月營收區域圖')
chart_data=data.set_index('月份')[['師大店營收', '內湖店營收']]
st.area_chart(
    chart_data,
    color=['#FF6B6B', '#4ECDC4'],
    x_label='月份',
    y_label='營收(單位:元)'    
    )



