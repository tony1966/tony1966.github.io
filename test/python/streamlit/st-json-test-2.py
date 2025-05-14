# st-json-test-2.py
import json
import streamlit as st

st.subheader('顯示 Python 串列')
data=['台積電', '中碳', '台泥', '玉山金']
st.json(data)
