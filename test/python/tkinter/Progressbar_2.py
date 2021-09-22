import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x150")

progressbar=ttk.Progressbar(win, length=250)   # 設定進度條長度
progressbar.pack()
ttk.Button(win, text="開始", command=progressbar.start).pack()
ttk.Button(win, text="停止", command=progressbar.stop).pack()
win.mainloop()