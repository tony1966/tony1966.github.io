# st-checkbox-test-1.py
import streamlit as st

label='接受全部 Cookies'
checked=st.checkbox(label)
if checked:
    st.write("您已勾選同意接受全部 Cookies")

