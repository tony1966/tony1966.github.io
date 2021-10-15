import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter.filedialog import askopenfilename, asksaveasfile

win=tk.Tk()                                                      
win.title("Simple Text Editor")
win.geometry("500x400")

def new_file():
    yes=msgbox.askyesno("確認", "要儲存目前的內容嗎?")
    if yes:
        save_file()
    text.delete(1.0, "end")
        
def old_file():
    file=askopenfilename(filetypes=(('text files', 'txt'),))
    with open(file, "r", encoding="utf-8") as f:
        text.insert("insert", f.read())      

def save_file():
    f=asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    f.write(text.get(1.0, "end"))
    f.close() 

def quit():
    yes=msgbox.askyesno("確認", "要儲存目前的內容嗎?")
    if yes:
        save_file()
    win.destroy()

def about():
    msgbox.showinfo("關於此軟體", "Simple Text Editor")

def version():
    msgbox.showinfo("版本", "v 1.0.0")

# add menu 
menubar=tk.Menu(win)
win.config(menu=menubar)
file_menu=tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="開新檔案", command=new_file)
file_menu.add_command(label="開啟舊檔", command=old_file)
file_menu.add_command(label="儲存檔案", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="關閉", command=quit)
menubar.add_cascade(label="檔案", menu=file_menu)
help_menu=tk.Menu(menubar, tearoff=False)
help_menu.add_command(label="版本", command=version)
help_menu.add_command(label="關於", command=about)
menubar.add_cascade(label="幫助", menu=help_menu)
# add editor
scrollbar=tk.Scrollbar(win)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)    
text=tk.Text(win, height=10, bg="aqua")
text.pack(side=tk.LEFT, fill=tk.Y)
text.config(padx=5, pady=5, font="Helvetic 12")  
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)          
win.mainloop()