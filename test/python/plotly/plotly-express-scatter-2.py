import pandas as pd
import plotly.express as px    
weight=[49, 65, 53, 45, 56, 47, 52, 61] # 體重
height=[159, 177, 156, 163, 164, 158, 166, 171] # 身高    
data=pd.DataFrame({'weight': weight, 'height': height})    
fig=px.scatter(data, x='weight', y='height') 
fig.show()
