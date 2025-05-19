# st-checkbox-test-3.py
import streamlit as st

st.subheader('擅長的程式語言 :')
prog1=st.checkbox('Python', value=True)
prog2=st.checkbox('C++')
prog3=st.checkbox('Javascript', value=True)
prog4=st.checkbox('PHP', value=True)
st.write('已勾選項目 :')
if prog1:
    st.write('Python')
if prog2:
    st.write('C++')
if prog3:
    st.write('Javascript')
if prog4:
    st.write('PHP')


