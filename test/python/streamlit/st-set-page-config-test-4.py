# st-set-page-config-test-4.py
import streamlit as st

st.set_page_config(initial_sidebar_state='collapsed')
# 側邊欄內容
st.sidebar.title('側邊欄')
st.sidebar.write('這是側邊欄的內容')
if st.sidebar.button('點擊我'):
    st.sidebar.write('你點擊了側邊欄按鈕！')
# 主頁面內容
st.title('主頁面')
st.write('這是主頁面的內容。')
