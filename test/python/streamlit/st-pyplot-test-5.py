# st-pyplot-test-5.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 顯示中文:使用微軟正黑體
plt.rcParams['font.family']=['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus']=False  # 正確顯示負號
# 建立隨機資料
rng=np.random.RandomState(0)
x=rng.randn(100)
y=rng.randn(100)
colors=rng.rand(100)
sizes=1000 * rng.rand(100)
# 建立圖表物件
fig, ax=plt.subplots()
# 繪製散佈圖
sc=ax.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='hsv')
# 添加色條
fig.colorbar(sc, ax=ax)
# 設定標題
ax.set_title('Matplotlib 隨機散佈圖')
st.pyplot(fig)
