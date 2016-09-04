from Tkinter import*
from tkFileDialog import*
import os
import pickle

def settings_open():
    os.chdir('settings')
    os.startfile('settings.exe')
    os.chdir('..')

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    try:
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except:
        saveAs()

def saveAs():   
    f = asksaveasfile(mode = 'w', defaultextension = '.gs')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        print('error')

def openFile():

    try:
        f = askopenfile(mode = 'r')
        print f
        t = f.read()
        print t 
        text.delete(0.0, END)
        text.insert(0.0, t)
    except:
        warn = Tk()
        warn.title('Waning!')
        warn.geometry('500x250')

        labelText = StringVar()
        labelText.set('''That file is not readable!
                         Try opening a .gs file!''')

        label1 = Label(warn, textvariable = labelText, height = 10)
        label1.pack()

        warn.mainloop()

def run():
    os.chdir('settings')
    pickle_in = open('compiler_ver.gsrf', 'r')
    compiler_ver = pickle.load(pickle_in)
    os.chdir('..')
    if compiler_ver == 'normal':
        f = asksaveasfile(mode = 'w', defaultextension = '.gs')
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            print('error')
        abs_path = os.path.abspath(f.name)
        os.chdir('Grid Script Compiler auto run')
        pickle_out = open('file_path.gsrf', 'w')
        pickle.dump(abs_path, pickle_out)
        pickle_out.close()    
        os.startfile('Grid_Script_Compiler.exe')
        os.chdir('..')
    if compiler_ver == 'experamental':
        f = asksaveasfile(mode = 'w', defaultextension = '.gs')
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            print('error')
        abs_path = os.path.abspath(f.name)
        os.chdir('Grid Script Compiler auto run experimental')
        pickle_out = open('file_path.gsrf', 'w')
        pickle.dump(abs_path, pickle_out)
        pickle_out.close()    
        os.startfile('Grid_Script_Compiler.exe')
        os.chdir('..')
    

app = Tk()
app.title('Grid Worksop: Text')
app.geometry('1000x1000')

text = Text(app, width = 1000, height = 1000)
text.pack()

menubar = Menu(app)
filemenu = Menu(menubar)
filemenu.add_command(label = 'New', command = newFile)
filemenu.add_command(label = 'Open', command = openFile)
filemenu.add_command(label = 'Save', command = saveFile)
filemenu.add_command(label = 'Save As', command = saveAs)
filemenu.add_separator()
filemenu.add_command(label = 'Quit', command = app.quit)
menubar.add_cascade(label = 'File', menu = filemenu)
settings = Menu(menubar)
settings.add_command(label = 'Settings', command = settings_open)
menubar.add_cascade(label = 'Settings', menu = settings)
Run = Menu(menubar)
Run.add_command(label = 'Run Program', command = run)
menubar.add_cascade(label = 'Run', menu = Run)

app.config(menu = menubar)
app.mainloop()