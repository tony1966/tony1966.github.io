# st-exception-test-1.py
import streamlit as st

st.subheader('異常 (exception) 訊息框')
try:
    result=1/0
except Exception as e:
    st.exception(e)
