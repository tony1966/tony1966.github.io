# st-date_input-test-4.py
import streamlit as st
from datetime import datetime

date_range=st.date_input('請選擇日期範圍 :', value=('2025-05-04', '2025-05-30'))
if isinstance(date_range, tuple) and len(date_range) == 2:
    st.write(f'起始日期：{date_range[0]}')
    st.write(f'結束日期：{date_range[1]}')
else:
    st.write('請選擇一個日期範圍')