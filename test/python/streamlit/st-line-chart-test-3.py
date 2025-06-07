# st-line-chart-test-3.py
import streamlit as st
import pandas as pd

df=pd.DataFrame({
    '日期': pd.date_range('2025-06-01', periods=7),
    '溫度': [28, 26, 25, 27, 30, 32, 31]
    })
st.subheader('一周氣溫變化')
st.line_chart(df, x='日期', y='溫度', width=150, height=400, use_container_width=False)

