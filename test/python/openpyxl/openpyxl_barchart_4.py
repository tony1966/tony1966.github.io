import openpyxl as xl
from openpyxl.chart import BarChart3D, Reference
wb=xl.Workbook()
ws=wb.active
dividend=[['年份', '0056殖利率', '0050殖利率'],        
          ['2015', 4.33, 3.01],
          ['2016', 5.67, 1.28],
          ['2017', 3.78, 6.1],
          ['2018', 5.62, 7.1],
          ['2019', 6.7, 7.22]]  
for row in dividend:    
    ws.append(row)
chart=BarChart3D()
chart.title='0056 vs 0050 殖利率'
chart.x_axis.title='ETF'
chart.y_axis.title='殖利率'
x=Reference(ws, min_col=1, max_col=1, min_row=2, max_row=ws.max_row)
y=Reference(ws, min_col=2, max_col=3, min_row=1, max_row=ws.max_row)  
chart.add_data(y, titles_from_data=True)
chart.set_categories(x)
ws.add_chart(chart, 'D1')
wb.save('ETF_dividend_yield_3D.xlsx')