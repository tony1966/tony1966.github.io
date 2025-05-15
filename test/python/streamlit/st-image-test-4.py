# st-image-test-4.py
import streamlit as st
from PIL import Image

image=Image.open('cat2.jpg') # 傳回 PIL.Image.Image 物件
st.subheader("顯示圖片 (PIL.Image.Image 物件)")
st.image(image, caption='**可愛的貓咪1**')
