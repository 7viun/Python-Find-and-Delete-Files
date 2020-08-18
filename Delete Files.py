import tkinter as tk
import os
import ctypes
from tkinter import filedialog
resultx=[]
def increase():
    name = tk.filedialog.askdirectory()
    textEntry.set(name)
def deletefile():
    filename=ent_1.get()
    path = os.path.abspath(filename)
    result=os.listdir(path)
    listtodel=[x for x in result if '.00' in x]
    for i in listtodel:
        os.remove(path+'\\'+i)
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None,'You Deleted Backup Files','AVN',0)
window = tk.Tk()

window.rowconfigure([0,1,2], minsize=50, weight=1)
window.columnconfigure([0,1], minsize=500, weight=1)

lbl_1=tk.Label(master=window,text='File Path:',foreground="white",  # Set the text color to white
    background="black")
lbl_1.grid(row=0,columnspan=2,sticky ="nsew")

textEntry = tk.StringVar()
ent_1=tk.Entry(master=window,textvariable = textEntry)
ent_1.grid(row=1,columnspan=2,sticky ="nsew")

btn_1=tk.Button(master=window,text="Choose File",command=increase)
btn_1.grid(row=2,column=0,sticky ="nsew")

btn_2=tk.Button(master=window,text="Delete Backup Files",command=deletefile)
btn_2.grid(row=2,column=1,sticky ="nsew")
window.mainloop()
window.destroy()
