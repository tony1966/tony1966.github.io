# st-plotly-test-2.py
import streamlit as st
import plotly.express as px
import pandas as pd

# 繪圖的資料
df=pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6, 7, 8],
    'y': [10, 15, 13, 17, 20, 18, 25, 22]
    })
# 建立 Figure 物件
fig=px.line(
    df,
    x='x',
    y='y',
    title='Plotly 繪製折線圖',
    markers=True  # 標示資料點
    )
fig.update_layout(xaxis_title='X 軸', yaxis_title='Y 軸')
# 在 Streamlit 顯示圖表
st.plotly_chart(fig)

