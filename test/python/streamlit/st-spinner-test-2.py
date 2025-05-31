# st-spinner-test-2.py
import streamlit as st
import time

st.subheader('用旋轉等待元件 st.spinner() 顯示等候訊息')
uploaded_file=st.file_uploader('請上傳 MP4 影片', type=['mp4'])
if uploaded_file:  # 檔案上傳完成
    st.write(f'📄 檔案名稱：**{uploaded_file.name}**')
    with st.spinner('處理中請耐心等候 ... '):  # 等候資料處理
        time.sleep(5)  # 這裡可以處理存檔, 轉檔, 解碼等耗時工作
    st.success('✅ 影片上傳成功, 請按 Play 播放.')
    st.video(uploaded_file)
else:  # 尚未選取檔案時顯示提示, 並停止執行等待上傳
    st.info('請上傳一個 MP4 檔案')  # 尚未上傳則提示
    st.stop()     # 停止 rerun 等待使用者選取檔案後再繼續執行程式