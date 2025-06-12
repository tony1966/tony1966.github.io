# bokeh-bar-test-2.py
from bokeh.plotting import figure, show

x=[1, 2, 3, 4, 5]  # x 軸資料
y=[120000, 135000, 99000, 150000, 170000]  # y 軸資料
# 建立 figure 物件
fig=figure(width=400, height=300, title='Bokeh 長條圖')
# 繪製長條圖
fig.vbar(x, top=y, width=0.5, color='red', alpha=0.5)  
show(fig)  # 顯示圖表