import tkinter as tk
from tkinter import ttk

def show_selection():
    result_label["text"]=var.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

spinbox_tk=tk.Spinbox(win, from_=-10, to=10, wrap=True)
spinbox_tk.pack()
spinbox_ttk=ttk.Spinbox(win, from_=-10, to=10, wrap=True)
spinbox_ttk.pack()
win.mainloop()