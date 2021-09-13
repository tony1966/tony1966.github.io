import tkinter as tk
from tkinter import ttk

def show_value_h(value):    
    label_h.config(text=value)
def show_value_v(value):    
    label_v.config(text=value)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("400x450")

var=tk.StringVar()
scale_h=tk.Scale(win,
                 orient="horizontal",
                 from_=-10.0,
                 to=10.0,
                 digits=5,
                 resolution=0.005,
                 command=show_value_h)
scale_h.pack()
label_h=tk.Label(win)
label_h.pack()
scale_v=tk.Scale(win,
                 length=280,
                 from_=-10.0,
                 to=10.0,
                 digits=4,
                 resolution=0.1,
                 command=show_value_v)
scale_v.pack()
label_v=tk.Label(win)
label_v.pack()
win.mainloop()