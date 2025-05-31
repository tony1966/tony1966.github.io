# st-progress-test-1-2.py
import streamlit as st
import time

st.subheader('進度條 st.progress()')
progress_bar=st.progress(0, text='任務處理中 ...')
for i in range(100):
    progress_bar.progress(i, text=f'目前進度：{i}%')    # 更新進度條數值與文字
    time.sleep(0.05)   # 模擬延遲
progress_bar.progress(100, text=f'目前進度：100%')
st.success("✅ 處理完成！")
