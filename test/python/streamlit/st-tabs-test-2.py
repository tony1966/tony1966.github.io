# st-tabs-test-2.py
import streamlit as st

st.subheader('📜 唐詩選集')
poems={
    '李白': '《靜夜思》\n\n床前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。',
    '杜甫': '《春望》\n\n國破山河在，城春草木深。感時花濺淚，恨別鳥驚心。',
    '王之涣': '《登鸛鵲樓》\n\n白日依山盡，黃河入海流。欲窮千里目，更上一層樓。'
    }
tabs=st.tabs(list(poems.keys()))
for tab, (author, content) in zip(tabs, poems.items()):
    with tab:
        st.markdown(content)