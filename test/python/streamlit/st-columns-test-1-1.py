# st-columns-test-1-1.py
import streamlit as st

col1, col2=st.columns(2)   # 傳回兩欄容器元件
col1.subheader('第一欄')   # 第一欄放置標題
col1.image('Lenna.jpg')  # 第一欄放置圖片
col2.subheader('第二欄')   # 第二欄放置標題
col2.image('Lenna.jpg')  # 第二欄放置圖片
