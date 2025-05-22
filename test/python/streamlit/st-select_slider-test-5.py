# st-select_slider-test-5.py
import streamlit as st

def on_slider_change(name):
    selected=st.session_state['fruit_choice']  # 取得追蹤之 key 的狀態
    fruits={'蘋果': 'apple', '葡萄': 'grape', '桃子': 'peach', '芒果': 'mango'}
    st.write(f'{name} 選的是：{fruits[selected]}')

label='請選擇最喜歡的水果 : '
options=['蘋果', '葡萄', '桃子', '芒果']
st.select_slider(label, options, key='fruit_choice', on_change=on_slider_change, kwargs={'name': 'Tony'})