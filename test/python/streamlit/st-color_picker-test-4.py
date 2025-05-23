# st-color_picker-test-4.py
import streamlit as st

def on_color_change(part):
    color_code=st.session_state['color_code']
    st.write(f'{part} 顏色已被修改為 : {color_code}')

part=st.text_input('請輸入修改部分：', '背景')
st.color_picker(
    '請選擇顏色 :',
    key='color_code',
    on_change=on_color_change,
    kwargs={'part': part}
    )
