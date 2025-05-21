# st-text_area-test-1.py
import streamlit as st

st.subheader('留言板')
msg=st.text_area('請輸入留言 :')
if msg:
    st.write(msg)


