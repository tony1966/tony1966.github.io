import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import time
import threading

def start_running_task(task, msg_start='作業執行中 ...', msg_end='已執行完成'):
    def check_thread():   # 檢查執行緒
        nonlocal start_time   # 參照外部變數
        if thread.is_alive():   # 執行緒還沒結束 : 繼續每 100 ms 檢查一次
            progress_win.after(100, check_thread) # 每 100 ms 檢查執行緒 
        else:  # 若執行緒已結束關閉進度條視窗            
            progress_win.destroy()
            end_time=time.time()
            elapsed=round(end_time - start_time, 2)   # 計算耗時
            msgbox.showinfo('通知訊息', f'{msg_end}, 耗時 {elapsed} 秒')
    start_time=time.time()  # 計算執行時間用
    # 建立 TopLevel 彈出視窗
    progress_win=tk.Toplevel(root)  
    progress_win.title('處理進度')
    progress_win.update_idletasks()  # 強制更新視窗更新, 處理所有事件
    progress_win.geometry('400x140')  # 將彈出視窗左上角拉到指定座標並設定大小
    progressbar=ttk.Progressbar(progress_win, mode='indeterminate', length=250)
    progressbar.pack(padx=3, pady=30)
    progressbar.start(5)   # 起始進度條並設定速度 (值越小跑越快)
    label=ttk.Label(progress_win)  # 顯示提示詞用
    label.config(text=msg_start, font=('Helvetica', 10, 'bold'))  # 設定字型大小
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
                        start_running_task(task))
start_button.pack()
root.mainloop()