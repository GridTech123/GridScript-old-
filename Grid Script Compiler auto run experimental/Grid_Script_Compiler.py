from tkFileDialog import*
import sys
import time
import pickle

dir = []

line = 0
length = 0
output = 0
var_names = []
var_values = []
modules = []

#f = askopenfile(mode = 'r')
#path = raw_input("What file path: ")

pickle_in = open('file_path.gsrf', 'r')
path = pickle.load(pickle_in)

try:
    t = open(path, 'r')
    print("________________________________________________________________________")
    print("starting " +str(path))
    print("________________________________________________________________________")  
    print ''
except:
    print("Somthing went wrong!")
    print('''It may be this:
1. it has to be a .gs or .txt file!
2. There cant be quotes(") in the path
3. Its not a path''')

lines = t.readlines()

while True:
    #print lines[line]
    line_reading = lines[line]
    printlength = len(line_reading)
    if line_reading[0:5] == 'print':
        if line_reading[6:18] == 'input.answer':
            try:
                print input_answer
            except:
                print '''ERROR!
can not print input_answer, this is
probably caused by not calling
input.ask'''               
        else:
            if line_reading[6:9] == 'var':
                printlength = len(line_reading)
                if line_reading[10:printlength - 1] in var_names:
                    var_read = line_reading[10:printlength - 1]
                    var_clock = 0
                    try:
                        var_found = False
                        while var_found == False:
                            if var_names[var_clock] == var_read:
                                var_found = True
                                print var_values[var_clock]
                            else:
                                var_clock = var_clock + 1
                    except:
                        print '''ERROR!
    can not print variable'''
                else:
                    print '''ERROR!
    not a variable'''
            else:
                printlength = len(line_reading)
                print line_reading[6:printlength]

    if line_reading[0:9] == 'app.quit':
        if 'app' in modules:
            sys.exit()
        else:
            print '''ERROR!
app not imported, use import app'''  

    if line_reading[0:4] == 'wait':
        try:
            printlength = len(line_reading)
            sleeplength = line_reading[5:printlength]
            #print sleeplength
            time.sleep(+int(sleeplength))
        except:
            print('''ERROR!
could not time.sleep''')

    if line_reading[0:3] == 'var':
        try:
            printlength = len(line_reading)
            var_names.append(line_reading[4:printlength - 1])   
            line = line + 1
            line_reading = lines[line]
            printlength = len(line_reading)
            var_values.append(line_reading[0:printlength - 1])   
        except:
            print '''ERROR!
could not make variable'''

    if line_reading[0:18] == 'app.variable.names':
        if 'app' in modules:
            try:
                print var_names
            except:
                print '''ERROR!
could not print var_names'''
        else:
            print '''ERROR!
app not imported, use import app'''            

    if line_reading[0:19] == 'app.variable.values':
        if 'app' in modules:
            try:
                print var_values
            except:
                print '''ERROR!
could not print var_values'''
        else:
            print '''ERROR!
app not imported, use import app'''   

    if line_reading[0:11] == 'app.modules':
        if 'app' in modules:
            try:
                print modules
            except:
                print '''ERROR!
could not print var_values'''
        else:
            print '''ERROR!
app not imported, use import app'''   

    if line_reading[0:6] == 'import':
        try:
            printlength = len(line_reading)
            if line_reading[7:printlength - 1] == 'app' or line_reading[7:printlength - 1] == 'input' or line_reading[7:printlength - 1] == 'graphics': 
                modules.append(line_reading[7:printlength - 1])
            else:
                print '''ERROR!
'''+str(line_reading[7:printlength - 1])+str(''' is not a module''')              
        except:
            print '''ERROR!
Could not modules.append'''

    if line_reading[0:9] == 'input.ask':
        if 'input' in modules:
            printlength = len(line_reading)
            input_answer = raw_input(line_reading[10:printlength - 1])
        else:
            print '''ERROR!
input not imported, use import input'''   

    if line_reading[0:2] == 'if': 
        printlength = len(line_reading)
        if line_reading[3:15] == 'input.answer':
            if 'input' in modules:   
                line = line + 1
                line_reading = lines[line]
                printlength = len(line_reading)
                if input_answer == line_reading[4:printlength - 1]:
                    line = line + 1
                    line_reading = lines[line]
                    printlength = len(line_reading)
                    if_true = True
                    if if_true == True:
                        line_reading = lines[line]
                        if line_reading[4:7] == 'end':
                            if_true == False
                            line = line + 1
                        if line_reading[4:12] == 'app.quit':
                            if 'app' in modules:
                                sys.exit()
                            else:
                                print '''ERROR!
app not imported, use import app''' 
                        #print lines[line]
                        line_reading = lines[line]
                        if line_reading[4:9] == 'print':
                            if line_reading[10:22] == 'input.answer':
                                try:
                                    print input_answer
                                except:
                                    print '''ERROR!
                    can not print input_answer, this is
                    probably caused by not calling
                    input.ask'''               
                            else:
                                if line_reading[10:19] == 'var':
                                    printlength = len(line_reading)
                                    if line_reading[20:printlength - 1] in var_names:
                                        var_read = line_reading[20:printlength - 1]
                                        var_clock = 0
                                        try:
                                            var_found = False
                                            while var_found == False:
                                                if var_names[var_clock] == var_read:
                                                    var_found = True
                                                    print var_values[var_clock]
                                                else:
                                                    var_clock = var_clock + 1
                                        except:
                                            print '''ERROR!
                        can not print variable'''
                                    else:
                                        print '''ERROR!
                        not a variable'''
                                else:
                                    printlength = len(line_reading)
                                    print line_reading[10:printlength]
                        line = line + 1
    line = line + 1
