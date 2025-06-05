# st-set-page-config-test-5.py
import streamlit as st

st.set_page_config(    
    menu_items={
        "Get help": "https://docs.streamlit.io",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": "這是一個示範用的 Streamlit App。"
        }
    )
st.subheader('st.set_page_config() 的 menu_items 參數')

