import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    h=float(height.get()) / 100
    w=float(weight.get())
    bmi=w / h ** 2
    if bmi < 18.5:
        comment="體重過輕"
    elif bmi >= 18.5 and bmi < 24:
        comment="體重適當"
    else:
        comment="體重過重"    
    msg=f"BMI 指數={bmi:.2f}, {comment}"
    result.set(msg)

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("350x150")

height=tk.DoubleVar()
weight=tk.DoubleVar()
result=tk.StringVar()
tk.Label(win, text="身高 (公分)").grid(row=0, column=0)
tk.Label(win, text="體重 (公斤)").grid(row=1, column=0)
tk.Entry(win, textvariable=height).grid(row=0, column=1)
tk.Entry(win, textvariable=weight).grid(row=1, column=1)
tk.Button(text="計算 BMI", command=calculate_bmi).grid(row=2, column=1)
tk.Label(win, textvariable=result).grid(row=3, columnspan=2, column=0)
win.mainloop()

