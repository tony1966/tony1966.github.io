import tkinter as tk
from tkinter import ttk

def show_value_h(value):    # 顯示水平滑桿值
    label_h.config(text=value)
def show_value_v(value):    # 顯示垂直滑桿值
    label_v.config(text=value)  

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x250")

scale_h=ttk.Scale(win, length=250)
scale_h["command"]=show_value_h
scale_h.pack()
label_h=ttk.Label(win)
label_h.pack()

scale_v=ttk.Scale(win, length=150)
scale_v["orient"]="vertical"
scale_v.config(command=show_value_v)
scale_v.pack()
label_v=ttk.Label(win)
label_v.pack()
win.mainloop()