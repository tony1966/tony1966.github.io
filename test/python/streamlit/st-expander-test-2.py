# st-expander-test-2.py
import streamlit as st

st.subheader('st.expander() 容器元件測試')
with st.expander('可愛的貓咪', expanded=True):
    st.write('我的貓咪相簿')
    st.image('https://yaohuang1966.github.io/images/cat1.jpg', width=200)
    st.image('https://yaohuang1966.github.io/images/cat2.jpg', width=200)
