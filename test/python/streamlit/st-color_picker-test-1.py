# st-color_picker-test-1.py
import streamlit as st

selected=st.color_picker('請選擇顏色 :')
if selected:
    st.write(selected)