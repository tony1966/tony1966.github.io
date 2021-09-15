import tkinter as tk
from tkinter import ttk

def show_selection():
    result_label["text"]=var.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

spinbox_tk=tk.Spinbox(win, from_=-1, to=1, increment=0.0005)
spinbox_tk["format"]="%5.4f"
spinbox_tk.pack()
spinbox_ttk=ttk.Spinbox(win, from_=-1, to=1, increment=0.0005)
spinbox_ttk.config(format="%5.4f")
spinbox_ttk.pack()
win.mainloop()