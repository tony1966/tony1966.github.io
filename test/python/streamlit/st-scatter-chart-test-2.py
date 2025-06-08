# st-scatter-chart-test-2.py
import streamlit as st
import pandas as pd

df=pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 70, 40, 60, 30],
    'group': ['A', 'B', 'A', 'B', 'A'],
    'value': [100, 200, 150, 300, 250]
    })
st.subheader('用 df.set_index() 指定索引繪製散布圖')
data=df.set_index('x')['y']  # 指定 x 欄為索引, y 欄為資料
st.scatter_chart(data=data)
