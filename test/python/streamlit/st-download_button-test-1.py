# st-download_button-test-1.py
import streamlit as st

text='Hello World!'
download=st.download_button(
    label='下載文字檔',
    data=text,
    file_name='hello.txt',
    mime='text/plain'
    )
if download:
    st.write('檔案已下載')