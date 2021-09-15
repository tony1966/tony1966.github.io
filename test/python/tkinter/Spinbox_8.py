import tkinter as tk
from tkinter import ttk

def show_value_tk():    
    label_tk.config(text=var_tk.get())
def show_value_ttk():
    label_ttk["text"]=var_ttk.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

var_tk=tk.StringVar()
var_tk.set(5)
spinbox_tk=tk.Spinbox(win,
                      from_=-10,
                      to=10,
                      textvariable=var_tk,
                      command=show_value_tk)
spinbox_tk.pack()
label_tk=tk.Label(win)
label_tk.pack()

var_ttk=tk.StringVar()
var_ttk.set(7)
spinbox_ttk=ttk.Spinbox(win,
                        from_=-10,
                        to=10,
                        textvariable=var_ttk,
                        command=show_value_ttk)
spinbox_ttk.pack()
label_ttk=ttk.Label(win)
label_ttk.pack()
win.mainloop()