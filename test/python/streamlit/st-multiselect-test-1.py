# st-multiselect-test-1.py
import streamlit as st

label='請選擇擅長的程式語言 : '
options=['Python', 'C++', 'Java', 'Javascript', 'PHP', 'Rust']
selected_items=st.multiselect(label, options) # 傳回串列
st.write("你選的是：", selected_items)

