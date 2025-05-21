# st-text_area-test-3.py
import streamlit as st

st.subheader('留言板')
msg=st.text_area('請輸入留言 :', placeholder='優良賣家', max_chars=100)
if msg:
    st.write(msg)


