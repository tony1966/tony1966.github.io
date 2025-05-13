# dataframe-4.py
import pandas as pd
import streamlit as st

score=[[78, 34, 65, 87, 99],   
       [100, 99, 89, 92, 100],   
       [88, 72, 95, 81, 100], 
       [67, 85, 73, 100, 56]]
index=['張三', '李四', '王五', '趙六']
columns=['國文', '英文', '數學', '自然', '社會']
df=pd.DataFrame(score, index=index, columns=columns)
st.subheader("成績單")
st.data_editor(df)