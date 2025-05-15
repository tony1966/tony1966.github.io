# st-image-test-1.py
import json
import streamlit as st

st.subheader("顯示圖片(預設參數)")
st.image('cat1.jpg')
st.subheader("顯示圖片(設定 width=740)")
st.image('cat1.jpg', width=740)
st.subheader("顯示圖片(設定 width=370)")
st.image('cat1.jpg', width=370)


