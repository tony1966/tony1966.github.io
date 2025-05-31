# st-spinner-test-1.py
import streamlit as st
import time

st.subheader('旋轉等待元件 st.spinner()')
with st.spinner('任務執行中, 請耐心等待'):
    time.sleep(15)
st.success("✅ 處理完成！")
