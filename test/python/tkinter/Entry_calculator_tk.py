import tkinter as tk
from tkinter import ttk

def add():
    c.set(a.get() + b.get())
def sub():
    c.set(a.get() - b.get())
def mul():
    c.set(a.get() * b.get())
def div():
    if b.get() != 0:
        c.set(a.get() / b.get())
    else:
        c.set(float("inf"))

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("500x200")
a=tk.DoubleVar()
b=tk.DoubleVar()
c=tk.DoubleVar()
tk.Entry(win, width=10, textvariable=a).grid(row=0, column=0)
tk.Label(win, text="+", width=5).grid(row=0, column=1)
tk.Entry(win, width=10, textvariable=b).grid(row=0, column=2)
tk.Button(win, text="=", width=5, command=add).grid(row=0, column=3)
tk.Entry(win, width=10, textvariable=c).grid(row=0, column=4)
tk.Label(win, text="-", width=5).grid(row=1, column=1)
tk.Button(win, text="=", width=5, command=sub).grid(row=1, column=3)
tk.Label(win, text="*", width=5).grid(row=2, column=1)
tk.Button(win, text="=", width=5, command=mul).grid(row=2, column=3)
tk.Label(win, text="/", width=5).grid(row=3, column=1)
tk.Button(win, text="=", width=5, command=div).grid(row=3, column=3)
win.mainloop()

