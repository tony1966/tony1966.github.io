# st-download_button-test-2.py
import streamlit as st

with open('sample.pdf', 'rb') as f:
    pdf_bytes=f.read()  # 讀取本地 PDF 檔案
    
st.download_button(
    label='下載 PDF 文件',
    data=pdf_bytes,
    file_name='downloaded_sample.pdf',
    mime='application/pdf'
    )