import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x200")
msg="人生就像騎腳踏車，想保持平衡就得往前走。"
label1=ttk.Label(win, text=msg, wraplength=200)
label1.config(relief="ridge")
label1.pack()
label2=ttk.Label(win, text=msg, wraplength=300, justify="left")
label2.config(relief="ridge")
label2.pack()
label3=ttk.Label(win, text=msg, wraplength=300, justify="right")
label3.config(relief="ridge")
label3.pack()

win.mainloop()
