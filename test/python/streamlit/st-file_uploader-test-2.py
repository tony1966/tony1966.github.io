# st-file_uploader-test-2.py
import streamlit as st
from PIL import Image

st.subheader('上傳多個檔案 (圖片)')
files=st.file_uploader(
    '請上傳圖片',
    type=['jpg', 'png', 'jpeg'],
    accept_multiple_files=True
    )
if files:
    for file in files:
        image=Image.open(file)
        st.image(file, caption=file.name)