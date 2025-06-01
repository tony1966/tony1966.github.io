# st-empty-test-1-3.py
import streamlit as st

st.subheader('st.empty() 容器元件測試')
placeholder=st.empty()
with placeholder.container():
    st.write('這在容器內')
    st.button('這在容器內')
    st.info('這在容器內', icon='ℹ️')
clear_btn=st.button('清除容器內容')
if clear_btn:
    placeholder.empty()
    st.info('容器內容已清除', icon='ℹ️')
