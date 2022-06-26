import openpyxl as xl
from openpyxl.chart import BarChart, Reference
wb=xl.Workbook()
ws=wb.active
votes=[['候選人', '得票數'],        
       ['宋楚瑜', 608590],    
       ['韓國瑜', 5522119],       
       ['蔡英文', 8170231]]
for row in votes:    
    ws.append(row)
chart=BarChart()
chart.title='2020 總統大選得票數'
chart.x_axis.title='候選人'
chart.y_axis.title='得票數'
x=Reference(ws, min_col=1, max_col=1, min_row=2, max_row=ws.max_row)
y=Reference(ws, min_col=2, max_col=2, min_row=1, max_row=ws.max_row)  
chart.add_data(y, titles_from_data=True)
chart.set_categories(x)
ws.add_chart(chart, 'C1')
wb.save('2020_presidential_2.xlsx')