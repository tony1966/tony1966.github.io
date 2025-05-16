# st-image-test-5.py
import streamlit as st
import numpy as np

st.subheader("Numpy 隨機生成的圖片")
image1=np.random.randint(0, 256, (300, 400, 3), dtype=np.uint8)
image2=np.random.randint(0, 256, (300, 400), dtype=np.uint8)
st.image([image1, image2], caption=['**彩色隨機圖**', '**灰階隨機圖**'], clamp=True)
