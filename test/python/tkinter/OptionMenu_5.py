# OptionMenu_5.py
import tkinter as tk

def show_change(*args):
    label['text']='You select ' + var.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("500x200")
var=tk.StringVar(win)
values=('Python', 'Java', 'C++', 'Perl')
optionmenu=tk.OptionMenu(win, var, *values)
optionmenu.pack()
label=tk.Label(win, text='')
label.pack()
var.trace('w', show_change)
win.mainloop()