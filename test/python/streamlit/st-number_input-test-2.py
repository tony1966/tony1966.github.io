# st-number_input-test-2.py
import streamlit as st

weight1=st.number_input('請輸入體重：', min_value=0.0, max_value=150.0, value=50.0, step=1.0)
st.write(f'您的體重是：{weight1}')


