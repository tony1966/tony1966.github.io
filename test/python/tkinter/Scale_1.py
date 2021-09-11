import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

scale_h=tk.Scale(win)
scale_h.pack()
scale_v=tk.Scale(win, orient=tk.HORIZONTAL)
scale_v.pack()
win.mainloop()