# st-multiselect-test-5.py
import streamlit as st

def on_multiselect_change(name=None):
    langs=st.session_state[f'langs']
    if langs:  # 檢查 key 之值
        st.write(f'{name} 選取了: {",".join(langs)}')
    else:
        st.write(f'{name} 未選取任何語言')

label='請選擇擅長的程式語言 : '
options=['Python', 'C++', 'Java', 'Javascript', 'PHP', 'Rust']
selected_items=st.multiselect(
    label,
    options,
    key='langs',
    on_change=on_multiselect_change,
    kwargs={'name': 'Tony'}
    ) # 傳回串列


