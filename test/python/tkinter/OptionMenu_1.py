# tkinter_optionmenu_1.py
import tkinter as tk

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("500x200")
var=tk.StringVar(win)
optionmenu=tk.OptionMenu(win, var, 'Python', 'Java', 'C++', 'Perl')
optionmenu.pack()
win.mainloop()