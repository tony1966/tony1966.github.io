# st-checkbox-test-6.py
import streamlit as st

def on_checked(lang=None):
    if st.session_state[f'prog_{lang}']:  # 檢查 key 之值
        st.write(f'{lang} 被選取了')
    else:
        st.write(f'{lang} 被取消選取了！')

st.subheader('擅長的程式語言 :')
langs=['Python', 'C++', 'JavaScript', 'PHP']
for lang in langs:
    st.checkbox(
        label=lang,
        key=f'prog_{lang}',
        on_change=on_checked,
        kwargs={'lang': lang}
        )

