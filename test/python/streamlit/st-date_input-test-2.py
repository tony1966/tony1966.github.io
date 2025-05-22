# st-date_input-test-2.py
import streamlit as st
from datetime import datetime

dt=datetime(2025, 5, 27, 0, 0)
date1=st.date_input('請選擇日期 :', key='date1', value=dt)
if date1:
    st.write(date1)
date2=st.date_input('請選擇日期 :', key='date2', value=dt.date())
if date2:
    st.write(date2)    
date3=st.date_input('請選擇日期 :', key='date3', value='2025-05-27')
if date3:
    st.write(date3)