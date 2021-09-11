import tkinter as tk
from tkinter import ttk

def show_value_h1(value):
    label_h1.set(var_h1.get())
def show_value_h2(value):
    label_h2.set(value)
def show_value_v(value):
    label_v.set(scale_v.get())

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x300")

var_h1=tk.IntVar()
scale_h1=tk.Scale(win,
                  variable=var_h1,
                  orient="horizontal",
                  command=show_value_h1)
scale_h1.pack()
label_h1=tk.StringVar()
tk.Label(win, textvariable=label_h1).pack()
scale_h2=tk.Scale(win,
                  orient="horizontal",
                  command=show_value_h2)
scale_h2.pack()
label_h2=tk.StringVar()
tk.Label(win, textvariable=label_h2).pack()
scale_v=tk.Scale(win, command=show_value_v)
scale_v.pack()
label_v=tk.StringVar()
tk.Label(win, textvariable=label_v).pack()
win.mainloop()