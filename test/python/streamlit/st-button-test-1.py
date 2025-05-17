# st-button-test-1.py
import streamlit as st

st.subheader('參數 type 測試')
btn1=st.button('type=primary 的按鈕', type='primary')
if btn1:  # 按下傳回 True
    st.write('你按了 type=primary 的按鈕')
btn2=st.button('type=secondary 的按鈕')
if btn2:  # 按下傳回 True
    st.write('你按了 type=secondary 的按鈕')    