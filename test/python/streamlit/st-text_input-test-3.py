# st-text_input-test-3.py
import streamlit as st

email=st.text_input(
    'E-mail：',
    placeholder='例如 abc@gmail.com (最長 50 字元)',
    max_chars=50
    )
st.write(f'你的 email : {email}')


