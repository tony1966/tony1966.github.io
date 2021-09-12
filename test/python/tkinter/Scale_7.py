import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x250")

scale_h=tk.Scale(win, width=40, length=150)
scale_h["bg"]="ivory"
scale_h["relief"]="ridge"
scale_h.pack()
scale_v=tk.Scale(win,
                 width=40,
                 length=250,
                 bg="cyan")
scale_v["orient"]="horizontal"
scale_v.config(relief="sunken", bg="cyan")
scale_v.pack()
win.mainloop()