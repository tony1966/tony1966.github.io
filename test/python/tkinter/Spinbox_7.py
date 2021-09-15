import tkinter as tk
from tkinter import ttk

def show_value_tk():
    label_tk["text"]=spinbox_tk.get()
def show_value_ttk():
    label_ttk.config(text=spinbox_ttk.get())

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

spinbox_tk=tk.Spinbox(win, from_=-10, to=10, command=show_value_tk)
spinbox_tk.pack()
label_tk=tk.Label(win)
label_tk.pack()
spinbox_ttk=ttk.Spinbox(win, from_=-10, to=10, command=show_value_ttk)
spinbox_ttk.pack()
label_ttk=ttk.Label(win)
label_ttk.pack()
win.mainloop()