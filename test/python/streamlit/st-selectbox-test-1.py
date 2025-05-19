# st-selectbox-test-1.py
import streamlit as st

label='請選擇最喜歡的水果 : '
options=['蘋果', '葡萄', '桃子', '芒果']
selection=st.selectbox(label, options)
st.write("你選的是：", selection)

