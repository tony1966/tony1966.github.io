import tkinter as tk
from tkinter import ttk

def show_selection():
    label_result["text"]="選擇結果: " + fruit.get()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試") 
fruit=tk.StringVar()
fruit.set("none")
tk.Label(text="請選擇最喜歡的水果 : ", width=30, bg="cyan").pack()
fruits={"apple": "蘋果", "grape": "葡萄", "peach": "桃子", "mango": "芒果"}
for value, text in fruits.items():
    tk.Radiobutton(win, text=text,
                   variable=fruit,
                   value=value,
                   command=show_selection).pack()
label_result=tk.Label(text="", width=30, bg="ivory")
label_result.pack()
win.mainloop()

