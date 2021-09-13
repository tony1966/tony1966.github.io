import tkinter as tk
from tkinter import ttk

def change_color(value):
    r=hex(scale_r.get())[2:]
    g=hex(scale_g.get())[2:]
    b=hex(scale_b.get())[2:]
    if len(r) < 2:
        r += "0"
    if len(g) < 2:
        g += "0"
    if len(b) < 2:
        b += "0"        
    color="#" + str(r) + str(g) + str(b)
    label.config(bg=color, text=color)
    

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("250x250")

scale_r=tk.Scale(win,
                 from_=0,
                 to=255,
                 label="R",
                 orient="horizontal",
                 command=change_color)
scale_r.set(0)
scale_r.grid(row=0, column=0)
scale_g=tk.Scale(win,
                 from_=0,
                 to=255,
                 label="G",
                 orient="horizontal",
                 command=change_color)
scale_g.set(0)
scale_g.grid(row=1, column=0)
scale_b=tk.Scale(win,                 
                 from_=0,
                 to=255,
                 label="B",
                 orient="horizontal",
                 command=change_color)
scale_b.set(0)
scale_b.grid(row=2, column=0)
label=tk.Label(win, bg="white", width=10, height=10)
label.grid(row=0, rowspan=3, column=1)
win.mainloop()