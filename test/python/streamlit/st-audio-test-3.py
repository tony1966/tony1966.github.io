# st-audio-test-3.py
import streamlit as st

st.subheader('播放 Byte 類型音訊')
with open('your_answer_clip.mp3', 'rb') as f:
    audio_bytes=f.read()
st.audio(audio_bytes, format='audio/mp3')