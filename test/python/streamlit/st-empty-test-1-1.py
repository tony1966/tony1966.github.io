# st-empty-test-1-1.py
import streamlit as st

st.subheader('st.empty() 容器元件測試')
st.write('這在容器外')
placeholder=st.empty()
container=placeholder.container()  # 取得可加入多元件之容器
container.write('這在容器內')
container.button('這在容器內')
container.info('這在容器內', icon='ℹ️')
st.write('這在容器外')
st.info('這在容器外', icon='ℹ️')
