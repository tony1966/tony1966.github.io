# st-number_input-test-5.py
import streamlit as st

st.subheader('format 參數測試')
st.number_input('整數', 0, 10, step=1, format='%d')
st.number_input('整數', 0.0, 10.0, step=0.1, format='%.0f')
st.number_input('一位小數', 0.0, 10.0, step=0.1, format='%.1f')
st.number_input('兩位小數', 0.0, 10.0, step=0.01, format='%.2f')