# st-checkbox-test-4.py
import streamlit as st

st.subheader('擅長的程式語言 :')
options={  # 定義核取方塊選項字典
    'prog1': 'Python',
    'prog2': 'C++',
    'prog3': 'Javascript',
    'prog4': 'PHP'
    }
# 初始化跨執行紀錄狀態字典鍵 programs
if 'programs' not in st.session_state:  
    st.session_state.programs=set()  # 用集合記錄被勾選之項目(避免重複)
for key, lang in options.items():  # 走訪選項字典
    checked=st.checkbox(lang, key=key)  # 建立核取方塊選項
    if checked:
        st.session_state.programs.add(lang)  # 被勾選語言加入集合
    else:
        st.session_state.programs.discard(lang)  # 取消勾選就移除
checked_items=', '.join(st.session_state.programs)  # 組成字串
st.write(f'已勾選項目 : {checked_items}')
