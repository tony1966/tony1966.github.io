import openpyxl as xl
from openpyxl.chart import PieChart3D, Reference
wb=xl.Workbook()
ws=wb.active
dividend=[['資產項目', '配置比率'],        
          ['股票', 60],
          ['基金', 20],
          ['現金', 10],
          ['黃金', 5],
          ['不動產', 5]]  
for row in dividend:    
    ws.append(row)
chart=PieChart3D()
chart.title='資產配置比例'
x=Reference(ws, min_col=1, max_col=1, min_row=2, max_row=ws.max_row)
y=Reference(ws, min_col=2, max_col=2, min_row=1, max_row=ws.max_row) 
chart.add_data(y, titles_from_data=True)
chart.set_categories(x)
ws.add_chart(chart, 'C1')
wb.save('asset_allocation_3D.xlsx')