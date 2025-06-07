# st-line-chart-test-1.py
import streamlit as st
import pandas as pd
import numpy as np

# 隨機資料
data=pd.DataFrame(
    np.random.randn(20, 3),
    columns=['甲', '乙', '丙']
    )
# 繪製折線圖
st.line_chart(data)

