import tkinter as tk
from tkinter import ttk
from tkinter import *


from scanSinglePort import fnScanPort as fnScanSinglePort
from scanMultiPort import fnScanPort as fnScanMultiPort

# ? global variables
blnPortModeSingle = False

# this is the function called when the button is clicked


# function to handle the button press to check for open ports
def fnStartPortScan():
    # TODO: Check if fields filled out
    if blnPortModeSingle:
        if fnCheckIfEmptyFields([objTbInpHost, objTbInpPort]):
            fnScanSinglePort(objTbInpHost.get(), objTbInpPort.get())
        else:
            print("Please fill in all fields")
    else:
        if fnCheckIfEmptyFields([objTbInpHost, objTbInpPort]):
            if objTbInpPort.get().count("-") == 1:
                if objTbInpSpeed.get() == "":
                    fltSpeed = 0.1
                else:
                    fltSpeed = float(objTbInpSpeed.get())
                fnScanMultiPort(objTbInpHost.get(), objTbInpPort.get().split(
                    "-")[0], objTbInpPort.get().split("-")[1], fltSpeed)
            else:
                print("Please enter a range of ports")
        else:
            print("Please fill in all fields")


# function to check if fields are empty
def fnCheckIfEmptyFields(arrFields):
    blnNoEmptyFields = True
    for field in arrFields:
        if field.get() == "":
            blnNoEmptyFields = False
    return blnNoEmptyFields

# create the root instance for the GUI
root = Tk()

# variable for radio buttons
objCheckBoxPicked = IntVar()
objCheckBoxPicked.set(2)


# function to handle radio buttons change
def fnRadioButtons():
    global blnPortModeSingle
    intCheckBoxPicked = objCheckBoxPicked.get()
    if (intCheckBoxPicked == 1):
        blnPortModeSingle = True
        objLblSpeed.place_forget()
        objTbInpSpeed.place_forget()
    else:
        blnPortModeSingle = False
        objLblSpeed.place(x=78, y=97)
        objTbInpSpeed.place(x=188, y=97)


# This is the section of code which creates the main window
root.geometry('560x320')
root.configure(background='#FFFAFA')
root.title('Welcome to port scanner')

# create and position the info field
Label(root, text='Fields with * are required', bg='#FFFAFA', font=(
    'arial', 12, 'normal')).place(x=78, y=7)

# create and position label for host
Label(root, text='Enter Host *', bg='#FFFAFA', font=(
    'arial', 12, 'normal')).place(x=78, y=37)


# create and position label for port
Label(root, text='Enter Port * ', bg='#FFFAFA', font=(
    'arial', 12, 'normal')).place(x=78, y=67)

# create and position label for speed
objLblSpeed = Label(root, text='Enter Speed', bg='#FFFAFA', font=(
    'arial', 12, 'normal'))
objLblSpeed.place(x=78, y=97)

# Create and position the host input box
objTbInpHost = Entry(root)
objTbInpHost.place(x=188, y=37)
objTbInpHost.insert(END, 'localhost')


# Create and position the port input box
objTbInpPort = Entry(root)
objTbInpPort.place(x=188, y=67)
if objCheckBoxPicked == 21: 
    objTbInpPort.insert(END, '80')
else:
    objTbInpPort.insert(END, '80-81')
    
# Create and position the speed input box
objTbInpSpeed = Entry(root)
objTbInpSpeed.place(x=188, y=97)
objTbInpSpeed.insert(END, '0.1')


arrModes = [('Single Port', 1), ('Multiple Ports', 2)]
frame = Frame(root, width=0, height=0, bg='#FFFAFA')
frame.place(x=58, y=127)
for txt, val in arrModes:
    Radiobutton(frame,
                text=txt,
                padx=20,
                variable=objCheckBoxPicked,
                command=fnRadioButtons,
                bg='#FFFAFA', font=('arial', 12, 'normal'),
                value=val).pack(side='left', anchor=W)

# create button to scan ports
Button(root, text='Check for open Port', bg='#FFFAFA', font=(
    'arial', 12, 'normal'), command=fnStartPortScan).place(x=78, y=170)
Button(root, text='Close Program', bg='#FFFAFA', font=(
    'arial', 12, 'normal'), command=root.destroy).place(x=248, y=170)


root.mainloop()
