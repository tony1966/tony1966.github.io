import tkinter as tk
from tkinter import ttk

def f2c():
    c.set((f.get() - 32) * 5/9)
def c2f():
    f.set(c.get() * 9/5 + 32)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("500x150")

f=tk.DoubleVar()
c=tk.DoubleVar()
tk.Label(win, text="華氏溫度").grid(row=0, column=0)
tk.Label(win, text="攝氏溫度").grid(row=0, column=2)
tk.Entry(win, textvariable=f).grid(row=1, rowspan=2, column=0)
tk.Button(text="=>", command=f2c).grid(row=1, column=1)
tk.Entry(win, textvariable=c).grid(row=1, rowspan=2, column=2)
tk.Button(text="<=", command=c2f).grid(row=2, column=1)
win.mainloop()

