# st-pyplot-test-3.py
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
st.subheader('今年 vs 去年前五個月營收比較')
# 準備資料
labels=data['月份']
今年=data['今年營收']
去年=data['去年營收']
x=np.arange(len(labels))  # 每個月的 x 座標
bar_width=0.35            # 長條寬度
# 建立圖表
fig, ax=plt.subplots()
ax.bar(x - bar_width/2, 去年, bar_width, label='去年營收', color='skyblue')
ax.bar(x + bar_width/2, 今年, bar_width, label='今年營收', color='orange')
# 美化圖表
ax.set_xlabel('月份')
ax.set_ylabel('營收')
ax.set_title('今年 vs 去年 每月營收比較')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.5)
# 顯示圖表
fig=plt.gcf()  # 取得目前的 Figure 物件
st.pyplot(fig)