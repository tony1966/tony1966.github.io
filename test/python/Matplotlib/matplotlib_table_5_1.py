import matplotlib.pyplot as plt

plt.rcParams["font.family"]=["Microsoft JhengHei"] 
columns=["股票名稱", "股票代號", "收盤價"]
data=[['元大台灣50', '0050', 111.55],
      ['元大高股息', '0056', 26.81],
      ['台積電', '2330', 453.5],
      ['聯電', '2303', 38.05],
      ['中華電', '2412', 124]]
plt.axis('off')
table=plt.table(cellText=data, colLabels=columns, loc="center",
                colColours=['yellow']*3)
for key, cell in table.get_celld().items():
    cell.set_facecolor('cyan')
plt.show()