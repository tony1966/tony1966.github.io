# st-set-page-config-test-2.py
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='我的儀表板',
    page_icon='📊'    
    )
st.subheader('預設頁面參數 layout="centered"')
df=pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f'欄 {i+1}' for i in range(20)]
    )
st.dataframe(df, use_container_width=True)
