# st-camera_input-test-1.py
import streamlit as st

picture=st.camera_input("請按 Take Photo 鈕拍照")
if picture:
    st.image(picture)
    st.write('已完成拍照')