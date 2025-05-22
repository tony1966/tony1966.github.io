# st-select_slider-test-2.py
import streamlit as st

label='請選擇最喜歡的水果 : '
options=['apple', 'grape', 'peach', 'mango']
fruits={'apple': '蘋果', 'grape': '葡萄', 'peach': '桃子', 'mango': '芒果'}
selection=st.select_slider(label, options, format_func=lambda x: fruits[x])
st.write("你選的是：", selection)