# st-area-chart-test-1.py
import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd
import numpy as np

# 模擬的時間序列資料
dates=pd.date_range('2025-04-01', periods=30)
data=pd.DataFrame(
    np.random.randn(30, 3).cumsum(axis=0),
    columns=['A', 'B', 'C'],
    index=dates
    )
st.subheader('一周氣溫變化')
st.area_chart(data)

