# st-time_input-test-3.py
import streamlit as st

def show_meeting_time(agenda):
    meeting_time=st.session_state['meeting_time']
    st.write(f'{agenda} 會議時間 {meeting_time}')

agenda=st.text_input('請輸入議程：', '年度計畫討論會')
st.time_input(
    '請選擇時間 :',
    key='meeting_time',
    on_change=show_meeting_time,
    args=(agenda,)
    )