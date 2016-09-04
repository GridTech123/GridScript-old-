from Tkinter import*
from tkFileDialog import*
import os
import pickle
import time

f = os.getcwd

def t():
    v_int = v.get()
    if v_int == 2:
        f = askdirectory()     

def save():
    v_int = v.get()
    if v_int == 2:
        pickle_out = open('open_at.gsrf', 'w')
        pickle.dump(f, pickle_out)
        pickle_out.close()    
    if v_int == 1:
        f = os.getcwd
        pickle_out = open('open_at.gsrf', 'w')
        pickle.dump(f, pickle_out)
        pickle_out.close()    

app = Tk()
app.title('Grid Script: settings')
app.geometry('500x250')

labelText = StringVar()
labelText.set('Where should we set your save/load location')
label1 = Label(app, textvariable = labelText, height = 4)
label1.pack()

v = IntVar()

Radiobutton(app, text="Go to cwd", variable=v, value=1).pack(anchor=W)
Radiobutton(app, text="Set to", variable=v, value=2).pack(anchor=W)

logbutton = Button(app, text = 'Open at', width = 10, command = t)
logbutton.pack(padx = 0, pady = 0)

logbutton = Button(app, text = 'save', width = 10, command = save)
logbutton.pack(padx = 0, pady = 0)

app.mainloop()