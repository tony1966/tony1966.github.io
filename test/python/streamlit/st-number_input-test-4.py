# st-number_input-test-4.py
import streamlit as st

def show_value(var):
    value=st.session_state[var]
    st.write(f'{var} 目前的數值是：{value}')

st.number_input('請輸入 A 之值：', key='A', on_change=show_value, kwargs={'var': 'A'})
st.number_input('請輸入 B 之值：', key='B', on_change=show_value, kwargs={'var': 'B'})

