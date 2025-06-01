# st-container-test-1-2.py
import streamlit as st

st.subheader('st.container() 容器元件測試')
st.write('這在容器外')
with st.container():
    st.write('這在容器內')
    st.button('這在容器內')
    st.info('這在容器內', icon='ℹ️')
st.write('這在容器外')
st.info('這在容器外', icon='ℹ️')
