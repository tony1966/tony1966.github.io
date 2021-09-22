import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

progressbar1=ttk.Progressbar(win, orient="vertical")
progressbar1.pack()
ttk.Button(win, text="開始", command=progressbar1.start).pack()
ttk.Button(win, text="停止", command=progressbar1.stop).pack()
win.mainloop()