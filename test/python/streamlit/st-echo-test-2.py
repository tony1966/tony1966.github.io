# st-echo-test-2.py
import streamlit as st

st.subheader('st.echo(code_location="below") 範例')
with st.echo(code_location='below'):
    st.write('位於 with st.echo() 區塊內')
    x=10
    y=20
    st.write(f'x + y = {x + y}')

