# st-image-test-3.py
import streamlit as st

with open('cat1.jpg', 'rb') as f:
    image=f.read()
    print(type(image))   # 顯示 <class 'bytes'>
    
st.subheader("顯示圖片 (Bytes 型別)")
st.image(image, caption='**可愛的貓咪1**')



