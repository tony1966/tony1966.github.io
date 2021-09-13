import tkinter as tk
from tkinter import ttk

def show_value_h1(value):
    scale_h1.config(label=var_h1.get())
def show_value_h2(value):
    scale_h2["label"]=value
def show_value_v(value):
    scale_v.configure(label=scale_v.get())

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x300")

var_h1=tk.IntVar()
scale_h1=tk.Scale(win,
                  variable=var_h1,
                  orient="horizontal",
                  command=show_value_h1)
scale_h1.pack()
scale_h2=tk.Scale(win,
                  orient="horizontal",
                  command=show_value_h2)
scale_h2.pack()
scale_v=tk.Scale(win, command=show_value_v)
scale_v.pack()
win.mainloop()