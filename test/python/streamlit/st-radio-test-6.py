# st-radio-test-6.py
import streamlit as st

def on_radio_change(name=None):
    selected=st.session_state['fruit_choice']
    fruits={'蘋果': 'apple', '葡萄': 'grape', '桃子': 'peach', '芒果': 'mango'}
    st.write(f'{name} 選的是：{fruits[selected]}')

label='請選擇最喜歡的水果 : '
options=['蘋果', '葡萄', '桃子', '芒果']
st.radio(label, options, key='fruit_choice', on_change=on_radio_change, kwargs={'name': 'Tony'})
