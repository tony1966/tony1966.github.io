# tkinter_optionmenu_2.py
import tkinter as tk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("500x200")
var=tk.StringVar(win)
values=('Python', 'Java', 'C++', 'Perl')
optionmenu=tk.OptionMenu(win, var, *values)
optionmenu.pack()
win.mainloop()