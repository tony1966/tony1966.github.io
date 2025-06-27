# st-radio-test-7.py
import streamlit as st

st.subheader('連動的 st.radio 選單測試')
# 圖片尺寸選項
food_options={
    '米食': ['炒飯', '蛋包飯', '咖哩飯'],
    '麵食': ['炒麵', '烏龍麵', '鍋燒麵']
    }
# 初始化 session 狀態變數 : 預設=米食之炒飯
if 'main_sel' not in st.session_state:
    st.session_state.main_sel='米食'  # 預設米食
if 'item_sel' not in st.session_state:
    st.session_state.item_sel=food_options['米食'][0]  # 預設炒飯
# 主食選單（更新連動食譜選單）
main=st.radio(
    '選擇主食',
    ['米食', '麵食'],
    index=['米食', '麵食'].index(st.session_state.main_sel)
    )
# 當主食選項更改時更新狀態變數
if main != st.session_state.main_sel:  
    st.session_state.main_sel=main  # 更新主食狀態
    st.session_state.item_sel=food_options[main][0]  # 更新品項狀態為第一個被選取
# 品項選單 (會依主食動態變化)
item_sel=st.radio(
    '選擇品項',
    food_options[st.session_state.main_sel],  # 依據主食設定品項的選項
    index=food_options[st.session_state.main_sel].index(st.session_state.item_sel)
    )
st.session_state.item_sel=item_sel  # 更新食譜狀態
st.write(f'{st.session_state.main_sel}:{st.session_state.item_sel}')

