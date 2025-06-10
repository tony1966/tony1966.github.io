# st-plotly-test-2.py
import streamlit as st
import plotly.express as px
import pandas as pd

# 繪圖的資料
df=pd.DataFrame({
    '月份': ['一月', '二月', '三月', '四月', '五月'],
    '今年營收': [120000, 135000, 99000, 150000, 170000],
    '去年營收': [110000, 125000, 95000, 145000, 160000]
    })
# 將寬表格式轉為長表格式方便繪圖
df_melted=df.melt(id_vars='月份', var_name='年度', value_name='營收')
# 建立 Figure 物件
fig=px.bar(
    df_melted,
    x='月份',
    y='營收',
    color='年度',
    barmode='group',
    title='今年與去年營收比較'
    )
# 在 Streamlit 顯示圖表
st.plotly_chart(fig)

