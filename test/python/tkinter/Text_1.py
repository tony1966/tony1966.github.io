import tkinter as tk
win=tk.Tk()
win.title("tkinter GUI 測試")
win.geometry("400x300")
text=tk.Text()
text.insert(tk.INSERT, "Hello World!\n")
text.insert(tk.INSERT, "你是在說哈囉嗎?")
text.pack()
win.mainloop()