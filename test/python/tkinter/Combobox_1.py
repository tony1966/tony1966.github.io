import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

values_1=("岳不群", "左冷禪", "定逸師太", "任盈盈", "令狐沖") 
combobox_1=ttk.Combobox(win, values=values_1)
combobox_1.pack()
values_2=("張無忌", "趙敏", "楊不悔", "朱九貞", "周芷若")
combobox_2=ttk.Combobox(win, values=values_2)
combobox_2.pack()
win.mainloop()