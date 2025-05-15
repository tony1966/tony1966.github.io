# st-image-test-2.py
import streamlit as st

st.subheader("顯示圖片(預設參數)")
url='https://upload.wikimedia.org/wikipedia/zh/thumb/3/34/Lenna.jpg/300px-Lenna.jpg'
st.image(url)
st.subheader("顯示圖片(設定 use_container_width=True)")
st.image(url, use_container_width=True)
st.subheader("顯示圖片(設定 width=200)")
st.image(url, width=200)


