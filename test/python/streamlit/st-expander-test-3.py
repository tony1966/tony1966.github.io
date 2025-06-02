# st-expander-test-3.py
import streamlit as st

st.subheader('📜 唐詩選集')
with st.expander('《靜夜思》李白'):
    st.markdown('''
    床前明月光，  
    疑是地上霜。  
    舉頭望明月，  
    低頭思故鄉。
    ''')
with st.expander('《登鸛鵲樓》王之涣'):
    st.markdown('''
    白日依山盡，  
    黃河入海流。  
    欲窮千里目，  
    更上一層樓。
    ''')
with st.expander('《春曉》孟浩然'):
    st.markdown('''
    春眠不覺曉，  
    處處聞啼鳥。  
    夜來風雨聲，  
    花落知多少。
    ''')
