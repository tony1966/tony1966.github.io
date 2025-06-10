# st-plotly-test-2.py
import streamlit as st
import plotly.express as px
import pandas as pd

# 繪圖的資料
df=pd.DataFrame({
    'weight': [49, 65, 53, 45, 56, 47, 52, 61],
    'height': [159, 177, 156, 163, 164, 158, 166, 171]
    })
# 建立 Figure 物件
fig=px.scatter(
    df,
    x='weight',
    y='height',
    title='體重 vs 身高 散佈圖',
    labels={'weight': '體重 (kg)', 'height': '身高 (cm)'}
    )
fig.update_traces(marker=dict(size=10, color='blue'))
# 在 Streamlit 顯示圖表
st.plotly_chart(fig)

