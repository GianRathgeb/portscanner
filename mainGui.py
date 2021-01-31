import tkinter as tk
from tkinter import ttk
from tkinter import * 


from scanSinglePort import fnScanPort


# this is the function called when the button is clicked
def btnClickFunction():
	fnScanPort(objTbInpHost.get(), objTbInpPort.get())



root = Tk()

# This is the section of code which creates the main window
root.geometry('560x320')
root.configure(background='#FFFAFA')
root.title('Hello, I\'m the main window')


# label for host
Label(root, text='Enter Host', bg='#FFFAFA', font=('arial', 12, 'normal')).place(x=78, y=37)


# label for port
Label(root, text='Enter Port', bg='#FFFAFA', font=('arial', 12, 'normal')).place(x=78, y=67)


# position of host input box
objTbInpHost=Entry(root)
objTbInpHost.place(x=168, y=37)


# position of port input box
objTbInpPort=Entry(root)
objTbInpPort.place(x=168, y=67)


# create button
Button(root, text='Check for open Port', bg='#FFFAFA', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=78, y=107)


root.mainloop()
