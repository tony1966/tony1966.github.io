import tkinter as tk
from tkinter import ttk

def show_value_tk(value):
    label_tk.set(value)
def show_value_ttk(value):
    label_ttk.set(value)  

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x250")

var_tk=tk.IntVar()
var_tk.set(20)
scale_tk=tk.Scale(win,
                  variable=var_tk,
                  command=show_value_tk)
scale_tk.pack()
label_tk=tk.StringVar()
tk.Label(win, textvariable=label_tk).pack()

var_ttk=tk.DoubleVar()
var_ttk.set(0.7071)
scale_ttk=ttk.Scale(win,
                    variable=var_ttk,
                    command=show_value_ttk)
scale_ttk.pack()
label_ttk=tk.StringVar()
label_ttk.set(0.7071)
tk.Label(win, textvariable=label_ttk).pack()
win.mainloop()