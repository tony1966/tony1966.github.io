# st-video-test-3.py
import streamlit as st

st.subheader('播放 Bytes 類型視訊')
with open('cat.mp4', 'rb') as f:
    video_bytes=f.read()
st.video(video_bytes, format='video/mp4')