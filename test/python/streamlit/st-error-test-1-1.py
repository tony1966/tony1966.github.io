# st-error-test-1-1.py
import streamlit as st

st.subheader('錯誤 (error) 訊息框')
st.error('這是預設的錯誤訊息框')
st.error('這是有 emoji 的錯誤訊息框', icon="❌")