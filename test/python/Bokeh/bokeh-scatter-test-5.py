# bokeh-scatter-test-5.py
from bokeh.plotting import figure, show

x=[0, 1, 2, 3, 4, 5]  # x 軸資料
y=[-5, -2, 6, 12, 4, 9]  # y 軸資料
fig=figure(width=400, height=300, title='Bokeh 散布圖')  # 建立 figure 物件
fig.scatter(
    x,
    y,
    marker='circle',
    size=20,
    line_width=3,
    fill_color='#ff0000',
    legend_label='測試資料'
    )  # 繪製圓點散布圖
fig.legend[0].location='top_left'  # 設定圖例位置為左上
show(fig)  # 顯示圖表