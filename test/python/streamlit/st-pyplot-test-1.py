# st-pyplot-test-1.py
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# 顯示中文:使用微軟正黑體
plt.rcParams['font.family']=['Microsoft JhengHei']    
x=np.array([1, 2, 3, 4])
y=np.array([10, 20, 25, 30])
# 繪製折線圖
plt.plot(x, y, color='blue', marker='o')  # 繪製線條並設置顏色和標記
plt.title('Matplotlib 折線圖 (函數式)')  # 設置標題
plt.xlabel('X 軸')  # X 軸標籤
plt.ylabel('Y 軸')  # Y 軸標籤
plt.grid(True)  # 顯示網格
# 顯示圖表
fig=plt.gcf()  # 取得目前的 Figure 物件
st.pyplot(fig)