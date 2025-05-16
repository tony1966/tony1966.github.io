# st-audio-test-2.py
import streamlit as st

st.subheader('播放網路 mp3 檔案')
audio_url='https://yaohuang1966.github.io/media/your_answer_clip.mp3'
st.audio(audio_url, format='audio/mp3')