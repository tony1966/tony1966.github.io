# st-progress-test-1-3.py
import streamlit as st
import time

st.subheader('進度條 st.progress()')
progress_bar=st.progress(0, text='任務處理中 ...')
st.button("❌ 取消任務", key='cancel')
for i in range(100):
    if st.session_state['cancel']:   # if st.session_state.cancel: 亦可
        progress_bar.progress(0, text='任務取消')
        st.warning('⚠️ 任務已取消')
        break
    progress_bar.progress(i + 1, text=f'目前進度：{i + 1}%')    # 更新進度條數值與文字
    time.sleep(0.05)   # 模擬延遲
if not st.session_state['cancel']:
    st.success("✅ 處理完成！")
