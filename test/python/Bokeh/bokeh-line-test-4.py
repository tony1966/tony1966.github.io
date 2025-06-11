# bokeh-line-test-4.py
from bokeh.plotting import figure, show

x=[0, 1, 2, 3, 4, 5]  # x 軸資料
y=[-5, -2, 6, 12, 4, 9]  # y 軸資料
fig=figure(
    width=400,
    height=300,
    title='Bokeh 折線圖',
    toolbar_location='below',
    background_fill_color='#ffff00'  # 黃色
    )  # 建立 figure 物件
fig.xgrid.visible=False # 取消 x 軸網格線
fig.line(
    x,
    y,
    line_width=4,
    line_dash='dotted',
    line_alpha=0.5,
    legend_label='測試資料'
    )  # 繪製折線圖
show(fig)  # 顯示圖表