# st-plotly-test-1.py
import streamlit as st
import plotly.graph_objs as go

# 繪圖的資料
weight=[49, 65, 53, 45, 56, 47, 52, 61] # 體重
height=[159, 177, 156, 163, 164, 158, 166, 171] # 身高
# 建立 Scatter 圖形物件
scatter=go.Scatter(
    x=weight,
    y=height,
    mode='markers',
    marker=dict(size=10, color='blue')
    )
# 建立 Layout 物件 (設定標題, 軸標籤等)
layout=go.Layout(
    title='體重 vs 身高 散佈圖',
    xaxis=dict(title='體重 (kg)'),
    yaxis=dict(title='身高 (cm)')
    )
# 建立 Figure 物件
fig=go.Figure(data=[scatter], layout=layout)
# 在 Streamlit 顯示圖表
st.plotly_chart(fig)

