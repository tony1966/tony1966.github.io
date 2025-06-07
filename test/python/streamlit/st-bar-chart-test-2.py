# st-bar-chart-test-2.py
import streamlit as st
import pandas as pd

# 模擬每月營收資料
data=pd.DataFrame({
    '月份': ['一月', '二月', '三月', '四月', '五月'],
    '營收': [120000, 135000, 99000, 150000, 170000]
    })
st.subheader('今年前五月月營收長條圖')
# 繪製 bar chart
chart_data=data.set_index('月份')['營收']
st.bar_chart(data=chart_data)
