import tkinter as tk
from tkinter import ttk

def show_value_h(value):    
    label_h.config(text=value)
def show_value_v(value):    
    label_v.config(text=value)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x450")

scale_h=tk.Scale(win,
                 length=280,
                 orient="horizontal",
                 tickinterval=10,
                 resolution=5,
                 command=show_value_h)
scale_h.pack()
label_h=tk.Label(win)
label_h.pack()
scale_v=tk.Scale(win,
                 length=280,
                 tickinterval=10,
                 resolution=20,
                 command=show_value_v)
scale_v.pack()
label_v=tk.Label(win)
label_v.pack()
win.mainloop()