# st-pyplot-test-2.py
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# 顯示中文:使用微軟正黑體
plt.rcParams['font.family']=['Microsoft JhengHei']    
x=np.array([1, 2, 3, 4])
y=np.array([10, 20, 25, 30])
# 建立子圖傳回 Figure 和 Axes 物件
fig, ax=plt.subplots()  
# 繪製折線圖
ax.plot(x, y, color='blue', marker='o')  # 在指定 Axes 上繪圖
ax.set_title('Matplotlib 折線圖 (物件導向)')  # 設置標題
ax.set_xlabel('X 軸')  # X 軸標籤
ax.set_ylabel('Y 軸')  # Y 軸標籤
ax.grid(True)  # 顯示網格
# 顯示圖表
st.pyplot(fig)