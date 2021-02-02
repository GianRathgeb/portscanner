import tkinter as tk
from tkinter import ttk
from tkinter import *


from scanSinglePort import fnScanPort

#? global variables
blnPortModeSingle = True

# this is the function called when the button is clicked
def btnClickFunction():
    # TODO: Check if fields filled out
    # TODO: function for single and multi mode
    if blnPortModeSingle:
        fnScanPort(objTbInpHost.get(), objTbInpPort.get())
    else:
        # TODO: Code for multi mode
        pass
    


root = Tk()

# variable for radio buttons
objCheckBoxPicked = IntVar()
objCheckBoxPicked.set(1)


def fnRadioButtons():
    intCheckBoxPicked = objCheckBoxPicked.get()
    if (intCheckBoxPicked == 1):
        blnPortModeSingle = True
    else:
        blnPortModeSingle = False

# This is the section of code which creates the main window
root.geometry('560x320')
root.configure(background='#FFFAFA')
root.title('Welcome to port scanner')


# label for host
Label(root, text='Enter Host', bg='#FFFAFA', font=(
    'arial', 12, 'normal')).place(x=78, y=37)


# label for port
Label(root, text='Enter Port', bg='#FFFAFA', font=(
    'arial', 12, 'normal')).place(x=78, y=67)


# position of host input box
objTbInpHost = Entry(root)
objTbInpHost.place(x=168, y=37)


# position of port input box
objTbInpPort = Entry(root)
objTbInpPort.place(x=168, y=67)


arrModes = [('Single Port', 1), ('Multiple Ports', 2)]
frame=Frame(root, width=0, height=0, bg='#FFFAFA')
frame.place(x=68, y=87)
for txt, val in arrModes:
    Radiobutton(frame,
                text=txt,
                padx=20,
                variable=objCheckBoxPicked,
                command=fnRadioButtons,
                bg='#FFFAFA', font=('arial', 12, 'normal'),
                value=val).pack(side='left', anchor=W)

# create button
Button(root, text='Check for open Port', bg='#FFFAFA', font=(
    'arial', 12, 'normal'), command=btnClickFunction).place(x=78, y=140)


root.mainloop()
