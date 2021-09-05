import tkinter as tk
from tkinter import ttk

def show_selection():
    selection=[]
    for i in range(0, len(languages)):
        if checkvar[i].get() == True:
            selection.append(languages[i])
    result_label["text"]="選取結果 : " + ",".join(selection)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試") 
ttk.Label(text="外語能力 : ", width=30, background="cyan").pack()
languages={0: "英語", 1: "日語", 2: "韓語"}
checkvar={}
for i in range(0, len(languages)):
    checkvar[i]=tk.BooleanVar()
    ttk.Checkbutton(win, text=languages[i],
                   variable=checkvar[i],
                   command=show_selection).pack()
result_label=ttk.Label(text="選取結果 : ", width=30, background="ivory")
result_label.pack()
win.mainloop()