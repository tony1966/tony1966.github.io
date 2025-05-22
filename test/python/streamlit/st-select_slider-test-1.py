# st-select_slider-test-1.py
import streamlit as st

label='請選擇最喜歡的水果 : '
options=['蘋果', '葡萄', '桃子', '芒果']
selection=st.select_slider(label, options)
st.write("你選的是：", selection)