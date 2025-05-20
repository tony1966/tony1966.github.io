# st-multiselect-test-3.py
import streamlit as st

label='請選擇擅長的程式語言 : '
options=['Python', 'C++', 'Java', 'Javascript', 'PHP', 'Rust']
default=['Python', 'Javascript']
selected_items=st.multiselect(label, options, default=default) # 傳回串列
st.write("你選的是：", selected_items)

