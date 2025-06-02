# st-sidebar-test-3.py
import streamlit as st
import pandas as pd

# 側邊欄：導覽選單
with st.sidebar:
    st.header('導航')
    page=st.radio('選擇頁面：', ['首頁', '資料', '關於'])

# 主頁面：根據側邊欄導覽頁的選擇顯示內容
st.title('應用程式')
if page == '首頁':
    st.write('歡迎來到首頁！這是應用程式的起始頁面。')
elif page == '資料':
    st.write('這裡是資料頁面，可以顯示資料表或圖表。')
    st.write(pd.DataFrame({'欄位1': [1, 2, 3], '欄位2': [4, 5, 6]}))
elif page == '關於':
    st.write('這是關於頁面，介紹應用程式的資訊。')
