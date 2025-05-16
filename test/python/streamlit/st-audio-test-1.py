# st-audio-test-1.py
import streamlit as st

st.subheader('播放本機 mp3 檔案')
with open('your_answer_clip.mp3', 'rb') as f:
    audio_bytes=f.read()
st.audio(audio_bytes, format='audio/mp3')