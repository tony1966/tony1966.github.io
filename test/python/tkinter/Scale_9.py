import tkinter as tk
from tkinter import ttk

def show_value_v(value):    
    label_v.config(text=value)
def show_value_h(value):    
    label_h.config(text=value)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x250")

scale_v=tk.Scale(win, showvalue=False, command=show_value_v)
scale_v.pack()
label_v=ttk.Label(win)
label_v.pack()

scale_h=tk.Scale(win, orient="horizontal", command=show_value_h)
scale_h.pack()
label_h=tk.Label(win)
label_h.pack()
win.mainloop()