# st-color_picker-test-2.py
import streamlit as st

selected=st.color_picker('請選擇顏色 :', value='#1177bb')
if selected:
    st.write(selected)