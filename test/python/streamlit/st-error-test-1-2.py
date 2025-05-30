# st-error-test-1-2.py
import streamlit as st

st.subheader('錯誤 (error) 訊息框')
try:
    result=1/0
except Exception as e:
    st.error(f'捕捉到除以 0 例外 ({e})', icon="❌")