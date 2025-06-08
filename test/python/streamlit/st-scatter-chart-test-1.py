# st-scatter-chart-test-1.py
import streamlit as st
import pandas as pd

df=pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 70, 40, 60, 30],
    'group': ['A', 'B', 'A', 'B', 'A'],
    'value': [100, 200, 150, 300, 250]
    })
st.subheader('預設的散布圖')
st.scatter_chart(
    data=df,
    x='x',
    y='y',
    #color='group',   # 依 group 欄位分類顏色
    #size='value',    # 依 value 欄位調整點大小
    #width=600,
    #height=400
    )
