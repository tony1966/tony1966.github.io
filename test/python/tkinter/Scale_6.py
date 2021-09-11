import tkinter as tk
from tkinter import ttk

def show_value_tk(value):
    label_tk.set(value)
def show_value_ttk(value):
    label_ttk.set(value)  

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x250")

scale_tk=tk.Scale(win,
                  from_=-10.0,
                  to=10.0,
                  command=show_value_tk)
scale_tk.pack()
label_tk=tk.StringVar()
tk.Label(win, textvariable=label_tk).pack()
scale_ttk=ttk.Scale(win,
                    from_=-10,
                    to=10,
                    command=show_value_ttk)
scale_ttk.pack()
label_ttk=tk.StringVar()
tk.Label(win, textvariable=label_ttk).pack()
win.mainloop()