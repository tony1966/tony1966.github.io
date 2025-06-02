# st-expander-test-1.py
import streamlit as st

st.subheader('st.expander() 容器元件測試')
expander=st.expander('可愛的貓咪')
expander.write('我的貓咪相簿')
expander.image('https://yaohuang1966.github.io/images/cat1.jpg', width=200)
expander.image('https://yaohuang1966.github.io/images/cat2.jpg', width=200)
