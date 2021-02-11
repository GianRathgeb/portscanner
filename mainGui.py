import tkinter as tk
from tkinter import ttk
from tkinter import *


from scanSinglePort import fnScanPort as fnScanSinglePort
from scanMultiPort import fnScanPort as fnScanMultiPort

# ? global variables
blnPortModeSingle = True

# this is the function called when the button is clicked


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


def fnCheckIfEmptyFields(arrFields):
    blnNoEmptyFields = True
    for field in arrFields:
        if field.get() == "":
            blnNoEmptyFields = False
    return blnNoEmptyFields


root = Tk()

# variable for radio buttons
objCheckBoxPicked = IntVar()
objCheckBoxPicked.set(1)


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

Label(root, text='Fields with * are required', bg='#FFFAFA', font=(
    'arial', 12, 'normal')).place(x=78, y=7)

# label for host
Label(root, text='Enter Host *', bg='#FFFAFA', font=(
    'arial', 12, 'normal')).place(x=78, y=37)


# label for port
Label(root, text='Enter Port * ', bg='#FFFAFA', font=(
    'arial', 12, 'normal')).place(x=78, y=67)

# label for port
objLblSpeed = Label(root, text='Enter Speed', bg='#FFFAFA', font=(
    'arial', 12, 'normal'))
objLblSpeed.place(x=78, y=97)

# position of host input box
objTbInpHost = Entry(root)
objTbInpHost.place(x=188, y=37)


# position of port input box
objTbInpPort = Entry(root)
objTbInpPort.place(x=188, y=67)

# position of port input box
objTbInpSpeed = Entry(root)
objTbInpSpeed.place(x=188, y=97)


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



#! When loading window
objTbInpSpeed.place_forget()
objLblSpeed.place_forget()

root.mainloop()
