# st-bar-chart-test-3.py
import streamlit as st
import pandas as pd

# 模擬每月營收資料
data=pd.DataFrame({
    '月份': ['一月', '二月', '三月', '四月', '五月'],
    '今年營收': [120000, 135000, 99000, 150000, 170000],
    '去年營收': [110000, 125000, 95000, 145000, 160000]
    })
st.subheader('今年 vs 去年前五個月營收比較')
# 繪製 bar chart
chart_data=data.set_index('月份')[['去年營收', '今年營收']]
st.bar_chart(data=chart_data)
