# st-json-test-3.py
import json
import streamlit as st

st.subheader("顯示 JSON 字串")
json_str='{"姓名": "金智媛", "性別": "女", "年齡": 32, "身高": 172.5, "已婚": false, "宗教": null}'
st.write(json_str)

obj=json.loads(json_str)
st.subheader("顯示 Python 字典")
st.write(obj, expanded=False)

st.subheader('顯示 Python 串列')
data=['台積電', '中碳', '台泥', '玉山金']
st.write(data)
