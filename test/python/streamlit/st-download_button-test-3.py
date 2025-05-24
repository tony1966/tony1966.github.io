# st-download_button-test-3.py
import streamlit as st

def on_click_download(original, downloaded):
    st.write(f'檔案 {original} 已被下載為 {downloaded}')

with open('sample.pdf', 'rb') as f:
    pdf_bytes=f.read()  # 讀取本地 PDF 檔案
    
st.download_button(
    label='下載 PDF 文件',
    data=pdf_bytes,
    file_name='downloaded_sample.pdf',
    mime='application/pdf',
    on_click=on_click_download,
    args=('sample.pdf', 'downloaded_sample.pdf')    
    )