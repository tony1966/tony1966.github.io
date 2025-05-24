# st-camera_input-test-3.py
import streamlit as st

def on_camera_change(name):
    picture=st.session_state['picture']
    if picture:
        st.image(picture, caption=f'**拍攝者 : {name}**')

picture=st.camera_input(
    '請按 Take Photo 鈕拍照',
    key='picture',
    on_change=on_camera_change,
    kwargs={'name': 'Tony'}
    )
