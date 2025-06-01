# st-container-test-1-1.py
import streamlit as st

st.subheader('st.container() 容器元件測試')
st.write('這在容器外')
container=st.container()
container.write('這在容器內')
container.button('這在容器內')
container.info('這在容器內', icon='ℹ️')
st.write('這在容器外')
st.info('這在容器外', icon='ℹ️')
