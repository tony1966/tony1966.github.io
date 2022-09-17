import plotly   
import plotly.graph_objs as go   
weight=[49, 65, 53, 45, 56, 47, 52, 61] # 體重
height=[159, 177, 156, 163, 164, 158, 166, 171] # 身高    
scatter=go.Scatter(x=weight, y=height, mode='markers') # 建立 Scatter 圖形物件
fig=go.Figure(scatter) # 依據所傳入之圖形物件建立 Figure 物件
fig.show() # 顯示圖形 
