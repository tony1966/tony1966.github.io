import tkinter as tk
from tkinter import ttk

def show_value_tk():
    label_tk["text"]=spinbox_tk.get()
def show_value_ttk():
    label_ttk.config(text=spinbox_ttk.get())

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

values_tk=("岳不群", "左冷禪", "定逸師太", "任盈盈", "令狐沖")
spinbox_tk=tk.Spinbox(win, from_=-10, to=10, values=values_tk)
spinbox_tk["command"]=show_value_tk
spinbox_tk.pack()
label_tk=tk.Label(win)
label_tk.pack()
values_ttk=["張無忌", "趙敏", "楊不悔", "朱九貞", "周芷若"]
spinbox_ttk=ttk.Spinbox(win, from_=-10, to=10, values=values_ttk)
spinbox_ttk["command"]=show_value_ttk
spinbox_ttk.pack()
label_ttk=ttk.Label(win)
label_ttk.pack()
win.mainloop()