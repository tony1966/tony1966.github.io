import matplotlib.pyplot as plt

def kbar(open, close, high, low, pos):
    if close > open:         # 上漲
        color='red'          # 紅 K 棒
        height=close - open  # 高度=收盤-開盤
        bottom=open          # 底部=開盤
    else:                    # 下跌
        color='green'        # 綠 k 棒
        height=open - close  # 高度=開盤-收盤
        bottom=close         # 底部=收盤
    # 繪製 k 棒實體      
    plt.bar(pos, height=height,bottom=bottom, width=0.2, color=color)
    # 繪製 k 棒上下影線
    plt.vlines(pos, high, low, color)

plt.rcParams["font.family"]=["Microsoft JhengHei"] # 字體=微軟正黑體 
day=['20190422','20190423','20190424','20190425','20190426','20190429','20190430']
kbar(10.2, 10.5, 9.5, 11, 0)       
kbar(10.5, 10, 10.6, 9.8, 1)       
kbar(10, 10.7, 10.9, 9.9, 2)       
kbar(10.7, 10.1, 10.9, 9.9, 3)     
kbar(10.1, 10.2, 10.5, 9.5, 4)     
kbar(10.2, 10.8, 10.8, 10.1, 5)    
kbar(10.8, 11.5, 10.8, 11.1, 6)    

plt.ylim(0, 15)  # 設定 y 軸範圍 
plt.xticks(range(len(day)), day)  # 設定 x 軸的刻度
plt.title('K線圖(2019-04-22 ~ 2019-04-30)')  
plt.show()  
