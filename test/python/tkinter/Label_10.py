import tkinter as tk
from tkinter import ttk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x300")
lenna=tk.PhotoImage(file="200x200-Lenna.png")
print(type(lenna))
msg="""影像處理教科書上著名的 Lenna 圖，取自於 1972 年 Playboy 雜誌上
模特兒 Lenna Söderberg 的照片。"""
label1=ttk.Label(win, text=msg, justify="left", image=lenna)
label1.config(relief="solid", padding=10, wraplength=200)
label1.pack()
win.mainloop()

