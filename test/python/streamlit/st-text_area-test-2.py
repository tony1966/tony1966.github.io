# st-text_area-test-2.py
import streamlit as st

st.subheader('留言板')
msg=st.text_area('請輸入留言 :', value='優良賣家', height=200)
if msg:
    st.write(msg)


