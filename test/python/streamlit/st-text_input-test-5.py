# st-text_input-test-5.py
import streamlit as st

def greet(punctuation):
    name=st.session_state.name
    st.write(f'您好! {name}{punctuation}')

st.text_input(
    label="輸入你的名字：",
    key='name',  # 必須設 key 才能使用 st.session_state
    on_change=greet,
    autocomplete='off',
    kwargs={'punctuation': '!'}  # 傳關鍵字參數
    )  



