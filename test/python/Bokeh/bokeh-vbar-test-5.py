# bokeh-bar-test-5.py
from bokeh.plotting import figure, show

x=[1, 2, 3, 4, 5]  # x 軸資料
y=[120000, 135000, 99000, 150000, 170000]  # y 軸資料
# 建立 figure 物件
fig=figure(width=400, height=300, title='Bokeh 長條圖')
# 繪製長條圖
fig.vbar(x, top=y, width=0.5, legend_label='今年前五月月營收')
fig.legend[0].location='top_left'  # 設定圖例位置為左上
show(fig)  # 顯示圖表