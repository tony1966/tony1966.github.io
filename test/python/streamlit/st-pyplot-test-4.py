# st-pyplot-test-4.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 顯示中文:使用微軟正黑體
plt.rcParams['font.family']=['Microsoft JhengHei']
# 模擬每月營收資料
data=pd.DataFrame({
    '月份': ['一月', '二月', '三月', '四月', '五月'],
    '今年營收': [120000, 135000, 99000, 150000, 170000],
    '去年營收': [110000, 125000, 95000, 145000, 160000]
    })
st.subheader('今年 vs 去年前五個月營收比較（水平長條圖）')
# 準備資料
labels=data['月份']
this_year=data['今年營收']
last_year=data['去年營收']
y=np.arange(len(labels))  # 每個月的 y 座標
bar_height=0.35           # 長條高度
# 建立圖表
fig, ax=plt.subplots()
ax.barh(y - bar_height/2, last_year, bar_height, label='去年營收', color='skyblue')
ax.barh(y + bar_height/2, this_year, bar_height, label='今年營收', color='orange')
# 設定圖表
ax.set_ylabel('月份')
ax.set_xlabel('營收')
ax.set_title('今年 vs 去年 每月營收比較')
ax.set_yticks(y)
ax.set_yticklabels(labels)
ax.legend()
ax.grid(axis='x', linestyle='--', alpha=0.5)
# 顯示圖表
st.pyplot(fig)
