# st-empty-test-1-4.py
import streamlit as st
import time

st.subheader('st.empty() 容器元件測試')
placeholder=st.empty()
with placeholder.container():
    st.info('正在處理中 ...', icon='ℹ️')
    time.sleep(5)
placeholder.empty()
st.info('處理完成!', icon='ℹ️')
