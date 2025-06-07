# st-line-chart-test-4.py
import streamlit as st
import pandas as pd
import numpy as np

# 建立 100 筆日氣溫資料
dates=pd.date_range('2025-01-01', periods=100)
data=pd.DataFrame({
    '日期': dates,
    '溫度': np.random.normal(loc=25, scale=2, size=100)
    })
# 建議使用說明提示
st.write('請選擇一個日期範圍（點兩次）')
# 設定日期範圍預設值: 最小與最大日期
date_selection=st.date_input(
    '選擇日期範圍',
    value=(dates.min(), dates.max()),
    min_value=dates.min(),
    max_value=dates.max()
    )
# 處理日期選取單日 unpack 問題, 不論回傳 1 或 2 都能正確 unpack
if isinstance(date_selection, tuple) and len(date_selection) == 2:
    start_date=pd.Timestamp(date_selection[0])
    end_date=pd.Timestamp(date_selection[1])
else:
    st.warning('請選擇起訖日期, 否則無法顯示圖表')
    st.stop()
# 篩選資料
mask=(data['日期'] >= start_date) & (data['日期'] <= end_date)
filtered_data=data.loc[mask]
# 顯示圖表
st.line_chart(
    data=filtered_data,
    x='日期',
    y='溫度',
    )
