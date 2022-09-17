import plotly   
import plotly.graph_objs as go   
weight=[49, 65, 53, 45, 56, 47, 52, 61] # 體重
height=[159, 177, 156, 163, 164, 158, 166, 171] # 身高    
data=go.Scatter(x=weight, y=height, mode='markers') # 建立 Scatter 圖形物件   
plotly.offline.plot({"data": [data]}) # 繪製圖形
