import tkinter as tk
from tkinter import ttk

def show_selection():
    label_result["text"]="選擇結果: " + fruit.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試") 
fruit=tk.StringVar()
fruit.set("none")
tk.Label(text="請選擇最喜歡的水果 : ", width=30, bg="cyan").pack()
fruits=["蘋果", "葡萄", "桃子", "芒果"]
for e in fruits:
    tk.Radiobutton(win, text=e,
                   variable=fruit,
                   value=e,
                   command=show_selection).pack()
label_result=tk.Label(text="", width=30, bg="ivory")
label_result.pack()
win.mainloop()

