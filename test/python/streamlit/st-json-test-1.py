# st-json-test-1.py
import json
import streamlit as st

st.subheader("顯示 JSON 字串")
json_str='{"姓名": "金智媛", "性別": "女", "年齡": 32, "身高": 172.5, "已婚": false, "宗教": null}'
st.json(json_str)
obj=json.loads(json_str)
st.subheader("顯示 Python 字典")
st.json(obj, expanded=False)