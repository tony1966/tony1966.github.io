# st-columns-test-1-4.py
import streamlit as st

col1, col2=st.columns(2)  # 傳回兩欄容器元件
with col1:
    st.subheader('第一欄')  # 第一欄放置標題
    st.image('Lenna.jpg')  # 第一欄放置圖片
with col2:
    st.subheader('第二欄')  # 第二欄放置標題
    st.image('Lenna.jpg')  # 第二欄放置圖片
col3, col4=st.columns(2, gap='large')  # 傳回兩欄容器元件
with col3:
    st.subheader('第一欄')  # 第一欄放置標題
    st.image('Lenna.jpg')  # 第一欄放置圖片
with col4:
    st.subheader('第二欄')  # 第二欄放置標題
    st.image('Lenna.jpg')  # 第二欄放置圖片