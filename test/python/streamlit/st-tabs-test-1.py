# st-tabs-test-1.py
import streamlit as st

st.subheader('📜 唐詩選集')
tab1, tab2, tab3=st.tabs(['李白', '杜甫', '王之涣'])
with tab1:
    st.markdown('《靜夜思》\n\n床前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。')
with tab2:
    st.markdown('《春望》\n\n國破山河在，城春草木深。感時花濺淚，恨別鳥驚心。')
with tab3:
    st.markdown('《登鸛鵲樓》\n\n白日依山盡，黃河入海流。欲窮千里目，更上一層樓。')
