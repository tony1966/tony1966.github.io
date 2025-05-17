# st-video-test-2.py
import streamlit as st

st.subheader('播放網路 mp4 檔案')
mp4_url='https://yaohuang1966.github.io/media/remind.mp4'
st.video(mp4_url, format='video/mp4')