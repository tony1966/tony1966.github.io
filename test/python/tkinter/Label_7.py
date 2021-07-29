import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x300")
lenna=tk.PhotoImage(file="200x200-Lenna.png")
print(type(lenna))
label1=ttk.Label(win, image=lenna)
label1.config(relief="solid", padding=10)
label1.pack()
win.mainloop()

