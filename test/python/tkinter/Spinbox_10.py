import tkinter as tk
from tkinter import ttk

def show_value_tk():
    label_tk["text"]=spinbox_tk.get()
def show_value_ttk():
    label_ttk.config(text=spinbox_ttk.get())

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

values_tk=(1, 3, 5, 7, 9, 11, 13, 15)
spinbox_tk=tk.Spinbox(win, values=values_tk)
spinbox_tk["command"]=show_value_tk
spinbox_tk.pack()
label_tk=tk.Label(win)
label_tk.pack()
values_ttk=[1.2, 4.3, 8.7, 9.3, 11.1, 13.2, 34.1, 78.9]
spinbox_ttk=ttk.Spinbox(win, values=values_ttk)
spinbox_ttk["command"]=show_value_ttk
spinbox_ttk.pack()
label_ttk=ttk.Label(win)
label_ttk.pack()
win.mainloop()