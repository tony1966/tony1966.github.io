# st-text_input-test-1.py
import streamlit as st

account=st.text_input('帳號：')
password=st.text_input('密碼：', type='password')
st.write(f'帳號 : {account}')
st.write(f'密碼 : {password}')

