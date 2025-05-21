# st-text_area-test-4.py
import streamlit as st

def on_text_change(user):
    comment=st.session_state['comment']
    st.write(f'{user} 留言 : {comment}')

st.subheader('留言板')
msg=st.text_area(
    '請輸入留言 :',
    key='comment',
    on_change=on_text_change,
    args=('匿名',)
    )


