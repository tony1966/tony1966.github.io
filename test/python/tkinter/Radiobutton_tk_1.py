import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox

def show_selection():
    msgbox.showinfo("info", "性別: " + gender.get())

win=tk.Tk()                                                      
win.title("tkinter GUI 測試") 
gender=tk.StringVar()
gender.set("M")
tk.Label(text="性別 : ", width=30, bg="cyan").pack()
tk.Radiobutton(win, text="男",
               variable=gender,
               value="M",
               command=show_selection).pack()
tk.Radiobutton(win, text="女",
               variable=gender,
               value="F",
               command=show_selection).pack()
win.mainloop()

