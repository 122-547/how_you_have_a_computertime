from tkinter import *
import messagebox
import time

def while_run():
    secs = 0
    while secs < 7200:
        Label(root, text=secs, font='Calibri 20').place(x=0, y=0)
        root.update()
        secs += 1
        time.sleep(1)
        
    messagebox.showinfo('INFO', 'Ты сидишь в компе уже 2ч, пора бы пройтись ;)')
    secs = 0
    while_run()

secs = 0
root = Tk()
root.resizable(0, 0)
root.geometry('120x40+0+0')
root.overrideredirect(1)
Label(root, text=secs, font='Calibri 20').place(x=0, y=0)

while_run()



