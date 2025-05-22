# st-date_input-test-1.py
import streamlit as st

selected=st.date_input('請選擇日期 :')
if selected:
    st.write(selected)