# st-plotly-test-4.py
import streamlit as st
import plotly.express as px
import pandas as pd

# 繪圖的資料
df=pd.DataFrame({
    'weight': [49, 65, 53, 45, 56, 47, 52, 61],
    'height': [159, 177, 156, 163, 164, 158, 166, 171]
    })
# 建立 Figure 物件
fig=px.scatter(df, x='weight', y='height')
fig.update_layout(
    title=dict(
        text='體重 vs 身高 散佈圖',
        x=0.4,  # 標題位置 (0=左, 1=右)
        font=dict(size=20, color='blue')
        ),
    xaxis=dict(title='體重 (kg)', range=[40, 70], showgrid=True),
    yaxis=dict(title='身高 (cm)', range=[150, 180], showgrid=True),
    legend=dict(x=0.8, y=1),
    width=700,
    height=500,
    margin=dict(l=50, r=50, t=80, b=50),
    plot_bgcolor='white',
    paper_bgcolor='lightgray',
    font=dict(family='Microsoft JhengHei', size=14),
    hovermode='closest'
    )
fig.update_traces(marker=dict(size=10, color='blue'))
# 在 Streamlit 顯示圖表
st.plotly_chart(fig)

