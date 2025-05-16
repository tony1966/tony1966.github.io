# st-audio-test-1.py
import streamlit as st

st.subheader('播放本機 mp3 檔案')
st.audio('your_answer_clip.mp3', format='audio/mp3')