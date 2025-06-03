# st-form-test-3.py
import streamlit as st

def on_submit_click():
    account=st.session_state['account']
    password=st.session_state['password']
    st.session_state['login_info']=f'帳號：{account}\n\n密碼：{password}'

with st.form(key='login_form'):
    account=st.text_input('帳號：', key='account')
    password=st.text_input('密碼：', key='password', type='password')
    st.form_submit_button(
        '提交',
        type='primary',
        on_click=on_submit_click,
        )
       
if 'login_info' in st.session_state:
    st.write(st.session_state['login_info'])
   