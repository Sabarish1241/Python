from logging import root
from tkinter import *
from tkinter.ttk import *
from time import strftime
 
root = Tk()
root.title("Sabarish_clock")
 
def time():
     string = strftime('%H:%M:%S:%p')
     label.config(text=string)
     label.after(1000, time)
     
label = Label(root, background = "black", foreground = "red")
label.pack(anchor='center')
time()

mainloop()
