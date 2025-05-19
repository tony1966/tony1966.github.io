# st-selectbox-test-3.py
import streamlit as st

def on_selectbox_change():
    selected=st.session_state['fruit_choice']  # 取得追蹤之 key 的狀態
    fruits={'蘋果': 'apple', '葡萄': 'grape', '桃子': 'peach', '芒果': 'mango'}
    st.write(f'你選的是：{fruits[selected]}')

label='請選擇最喜歡的水果 : '
options=['蘋果', '葡萄', '桃子', '芒果']
st.selectbox(label, options, key='fruit_choice', on_change=on_selectbox_change)