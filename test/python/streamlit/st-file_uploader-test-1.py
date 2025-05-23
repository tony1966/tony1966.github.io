# st-file_uploader-test-1.py
import streamlit as st
from PIL import Image

st.subheader('上傳單一檔案 (圖片)')
file=st.file_uploader('請上傳圖片', type=['jpg', 'png', 'jpeg'])
if file:
    image=Image.open(file)
    st.image(file, caption=file.name)