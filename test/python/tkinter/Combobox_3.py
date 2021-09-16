import tkinter as tk
from tkinter import ttk

def show_value():
    label["text"]="選取 : " + combobox.get() + \
                  " 索引 : " + str(combobox.current())

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

values=("Python", "Javascript", "R", "Julia", "PHP")
combobox=ttk.Combobox(win, values=values)
combobox.pack()
combobox.set("Python")        # 設定被選取選項
ttk.Button(win, text="確定", command=show_value).pack()
label=ttk.Label(win)
label.pack()
win.mainloop()