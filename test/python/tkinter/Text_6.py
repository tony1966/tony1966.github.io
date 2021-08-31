import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox

win=tk.Tk()                                                      
win.title("tkinter GUI 測試")                           
win.geometry("400x300")                                 
text=tk.Text(win, width=30, height=10, bg="aqua")
text.config(padx=5, pady=5, font="Helvetic 12")
text.insert("insert", "Hello World!\n")
text.insert("insert", "你是在說哈囉嗎?")
text.pack()

def get_all_content():
    content=text.get(1.0, "end")
    msgbox.showinfo("Info", content)    

def get_marked_index():
    try:
        start=text.index("sel.first")
        stop=text.index("sel.last")
        content="起始字元索引=" + start + " 結束字元索引=" + stop
        msgbox.showinfo("Info", content)
    except:
        msgbox.showinfo("Info", "請選取內容")
    
    
btn1=ttk.Button(win, text="顯示選擇內容起訖索引", command=get_marked_index)
btn1.pack()
win.mainloop()