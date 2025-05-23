# st-time_input-test-2.py
import streamlit as st
from datetime import time, timedelta

default_time=time(8, 30)
step=timedelta(minutes=10)
selected=st.time_input('請選擇時間 :', value=default_time, step=step)
if selected:
    st.write(selected)