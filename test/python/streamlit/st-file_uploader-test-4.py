# st-file_uploader-test-4.py
import streamlit as st

def on_upload_change(label):
    st.success(f'{label}檔案已上傳！')
    file=st.session_state['file']
    if file:
        st.write(f'檔名：{file.name}')
        st.write(f'大小：{file.size} bytes')

st.file_uploader(
    '請上傳檔案',
    type=['txt', 'pdf', 'docx'],
    key='file',
    on_change=on_upload_change,
    kwargs={'label': '機密'}
    )
