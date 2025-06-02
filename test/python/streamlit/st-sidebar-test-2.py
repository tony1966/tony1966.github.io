# st-sidebar-test-2.py
import streamlit as st

# 側邊欄內容
with st.sidebar:
    st.title('側邊欄')
    st.write('這是側邊欄的內容')
    if st.button('點擊我'):
        st.write('你點擊了側邊欄按鈕！')
# 主頁面內容
st.title('主頁面')
st.write('這是主頁面的內容。')
