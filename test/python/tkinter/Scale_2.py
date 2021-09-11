import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

scale_h=ttk.Scale(win)
scale_h.pack()
scale_v=ttk.Scale(win, orient=tk.VERTICAL)
scale_v.pack()
win.mainloop()