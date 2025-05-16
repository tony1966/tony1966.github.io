# st-image-test-6.py
import cv2
import streamlit as st

st.subheader('顯示 OpenCV 讀取的圖片')
image=cv2.imread('cat2.jpg')  # 使用 OpenCV 讀取BGR 格式圖片
print(type(image))  # <class 'numpy.ndarray'>
image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 轉為 RGB 格式
st.image(image_rgb, caption='**可愛的貓咪**')
