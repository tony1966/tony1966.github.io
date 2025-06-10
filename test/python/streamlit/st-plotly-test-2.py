# st-plotly-test-2.py
import streamlit as st
import plotly.express as px

# 繪圖的資料
weight=[49, 65, 53, 45, 56, 47, 52, 61] # 體重
height=[159, 177, 156, 163, 164, 158, 166, 171] # 身高
data={'weight': weight, 'height': height} # 打包成字典
# 建立 Figure 物件
fig=px.scatter(
    data,
    x='weight',
    y='height',
    title='體重 vs 身高 散佈圖',
    labels={'weight': '體重 (kg)', 'height': '身高 (cm)'}
    )
fig.update_traces(marker=dict(size=10, color='blue'))
# 在 Streamlit 顯示圖表
st.plotly_chart(fig)

