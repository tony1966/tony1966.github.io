# st-multiselect-test-2.py
import streamlit as st

label='請選擇擅長的程式語言 : '
options=['Python', 'C++', 'Java', 'Javascript', 'PHP', 'Rust']
placeholder='請選取選項 (可多選)'
selected_items=st.multiselect(label, options, placeholder=placeholder) # 傳回串列
st.write("你選的是：", selected_items)

