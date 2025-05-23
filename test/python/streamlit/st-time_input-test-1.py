# st-time_input-test-1.py
import streamlit as st

selected=st.time_input('請選擇時間 :')
if selected:
    st.write(selected)