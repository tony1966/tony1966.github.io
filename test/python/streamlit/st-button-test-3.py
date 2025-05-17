# st-button-test-3.py
import streamlit as st

def say_hello(name, greeting="Hello"):
    st.write(f'{greeting}, {name}!')
    
kwargs={'name': 'Tony', 'greeting': 'Hi'}
st.button("打招呼", on_click=say_hello, kwargs=kwargs)
