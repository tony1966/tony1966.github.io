# st-button-test-2.py
import streamlit as st

def say_hello(name):
    st.write(f'Hello! {name}')

name='Tony'
st.button('打招呼', on_click=say_hello, args=(name,))

