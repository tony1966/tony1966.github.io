import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox
import time
import threading

def start_running_task(task, msg='作業執行中 ...'):
    def check_thread(result):   # 檢查執行緒, result 為 task() 之傳回值
        nonlocal start_time     # 參照外部變數
        if thread.is_alive():   # 執行緒還沒結束 : 繼續每 100 ms 檢查一次
            progress_win.after(100, check_thread) # 每 100 ms 檢查執行緒 
        else:  # 若執行緒已結束關閉進度條視窗            
            progress_win.destroy()
            end_time=time.time()
            elapsed=round(end_time - start_time, 2)   # 計算耗時
            msgbox.showinfo('通知訊息', f'{result}\n耗時 {elapsed} 秒')
    def run_task():   # 中介函式
        result=task()     # 取得作業函式傳回值
        progress_win.after(100, check_thread, result)  # 每 100 ms 檢查執行緒是否還存活

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
    label.config(text=msg, font=('Helvetica', 10, 'bold'))  # 設定字型大小
    label.pack(padx=3, pady=3)    
    thread=threading.Thread(target=run_task)  # 建立執行緒執行中介函式 run_task()
    thread.start()    # 啟始執行緒

def job():
    time.sleep(5)   # 模擬漫長的執行時間
    error=2
    return '執行作業已完成, 錯誤數=' + str(error)

root=tk.Tk()
root.title('執行緒測試')
root.geometry('600x400')
start_button=ttk.Button(root, text='開始執行', command=lambda: \
                        start_running_task(job))
start_button.pack()
root.mainloop()