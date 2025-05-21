# st-number_input-test-1.py
import streamlit as st

age=st.number_input('請輸入年齡：', min_value=0, max_value=120, value=25, step=1)
st.write(f'您的年齡是：{age}')

