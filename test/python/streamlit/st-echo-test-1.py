# st-echo-test-1.py
import streamlit as st

st.subheader('st.echo() 範例')
with st.echo():
    st.write('位於 with st.echo() 區塊內')
    x=10
    y=20
    st.write(f'x + y = {x + y}')

