# st-form-test-1.py
import streamlit as st

with st.form(key='login_form'):
    account=st.text_input('帳號：')
    password=st.text_input('密碼：', type='password')
    if st.form_submit_button('提交', type='primary'):
        st.write(f'帳號：{account}')
        st.write(f'密碼：{password}')     

   