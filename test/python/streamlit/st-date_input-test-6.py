# st-date_input-test-6.py
import streamlit as st

def show_birthday_msg(name):
    st.write(f'祝 {name} {st.session_state["birthday"]} 生日快樂！')

name=st.text_input('請輸入名字：', 'Tony')
st.date_input(
    '請選擇日期 :',
    key='birthday',
    on_change=show_birthday_msg,
    args=(name,)
    )
