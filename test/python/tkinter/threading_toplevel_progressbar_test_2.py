import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import time
import threading

def start_running_task(task, msg):
    def check_thread():   # 檢查執行緒
        if thread.is_alive():   # 執行緒還沒結束 : 繼續每 100 ms 檢查一次
            progress_win.after(100, check_thread) # 每 100 ms 檢查執行緒 
        else:  # 若執行緒已結束關閉進度條視窗            
            progress_win.destroy()
            msgbox.showinfo('通知訊息', '執行作業已完成')
    # 建立 TopLevel 彈出視窗
    progress_win=tk.Toplevel(root)  
    progress_win.title('處理進度')
    progress_win.update_idletasks()  # 強制更新視窗更新, 處理所有事件
    # 設定彈出視窗左上角座標與大小始其置中
    width=400   # 彈出視窗寬度
    height=140  # 彈出視窗高度    
    screen_width=progress_win.winfo_screenwidth()    # 取得彈出視窗寬度
    screen_height=progress_win.winfo_screenheight()  # 取得彈出視窗高度
    x=(screen_width // 2) - (width // 2)    # 彈出視窗的左上角 x 座標
    y=(screen_height // 2) - (height // 2)  # 彈出視窗的左上角 y 座標  
    geometry=f'{width}x{height}+{x}+{y}'    # 設定視窗左上角座標與大小
    progress_win.geometry(geometry)  # 將彈出視窗左上角拉到指定座標並設定大小
    progressbar=ttk.Progressbar(progress_win, mode='indeterminate', length=250)
    progressbar.pack(padx=3, pady=30)
    progressbar.start(5)   # 起始進度條並設定速度 (值越小跑越快)
    label=ttk.Label(progress_win)  # 顯示提示詞用
    label.config(text=msg, font=('Helvetica', 10, 'bold'))  # 設定字型大小
    label.pack(padx=3, pady=3)    
    thread=threading.Thread(target=task)  # 建立執行緒
    thread.start()    # 啟始執行緒
    progress_win.after(100, check_thread)  # 每 100 ms 檢查執行緒是否還存活    

def task():
    time.sleep(10)   # 模擬漫長的執行時間

root=tk.Tk()
root.title('執行緒測試')
root.geometry('600x400')
start_button=ttk.Button(root, text='開始執行', command=lambda: \
                        start_running_task(task, '執行中請稍候 ...'))
start_button.pack()
root.mainloop()