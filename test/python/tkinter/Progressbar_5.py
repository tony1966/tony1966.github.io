import tkinter as tk
from tkinter import ttk
import time

def get_current_value():
    return "目前進度 : " + str(progressbar["value"]) + "%"
def start():    
    for i in range(progressbar["maximum"]):
        if progressbar["value"] < progressbar["maximum"]:
            progressbar["value"] += 1
            label["text"]=get_current_value()
            win.update()
            time.sleep(0.1)
        else:
            label["text"]="已完成!"
        
def stop():
    progressbar.stop()
    label["text"]=get_current_value()

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")
win.geometry("300x200")

progressbar=ttk.Progressbar(win, length=250, mode="determinate")
progressbar.pack()
ttk.Button(win, text="開始", command=start).pack()
ttk.Button(win, text="停止", command=stop).pack()
label=ttk.Label(win)
label.pack()
win.mainloop()