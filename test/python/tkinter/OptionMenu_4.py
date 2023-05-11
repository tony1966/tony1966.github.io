# OptionMenu_4.py
import tkinter as tk
from tkinter import messagebox

def event_handler():
    messagebox.showinfo('Info', 'You select ' + var.get())
    
win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("500x200")
var=tk.StringVar(win)
var.set('C++')
optionmenu=tk.OptionMenu(win, var, 'Python', 'Java', 'C++', 'Perl')
optionmenu.pack()
button=tk.Button(win, text='Get selection', command=event_handler)
button.pack()
win.mainloop()