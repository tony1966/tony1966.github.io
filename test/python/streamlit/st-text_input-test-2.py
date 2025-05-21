# st-text_input-test-2.py
import streamlit as st

email=st.text_input('E-mail：', value='abc@gmail.com')
st.write(f'你的 email : {email}')


