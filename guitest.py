from tkinter import *
from resources.classes.Windows import NewWindow

#Create window
window = Tk()

#Configure Window settings
window.title("Hello World")
window.geometry('350x200')
window.iconbitmap("resources/images/Support_Icon.ico")

#function for buttons
def clicked():
    result = "You wrote: " + txt.get()
    lbl.configure(text = result)
    txt.delete(0,END)

def reset():
    txt.delete(0,END)
    lbl.configure(text = "Test Words for input")

def closeProgram():
    window.quit()

def createWindow():
    NewWindow(window, "New Window")

#Menu bar
menu_bar = Menu(window)

#Create menu
menu_1 = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=menu_1)
menu_1.add_command(label='New', command=reset)
menu_1.add_separator()
menu_1.add_command(label='Exit',command=closeProgram)
window.config(menu=menu_bar)

#Window Content
lbl = Label(window, text="Test Words for input")
lbl.grid()

#Entry Field
txt = Entry(window, width=10)
txt.grid(column=1, row=0)

#Configure buttons
btn = Button(window, text = "Click Here", fg = "red", command=clicked)
btn_reset = Button(window, text = "Reset", fg = "Black", command=reset)
btn_close = Button(window, text='Close', fg = "Black", command=closeProgram)
btn_createwindow = Button(window, text="New Window", fg = "Black", command=createWindow)

#Set buttons to grid
lbl.grid (column=0, row=0)
btn.grid (column=1, row=1)
btn_reset.grid (column=2, row=1)
btn_close.grid(column=1, row=2)
btn_createwindow.grid(column=1, row=3)

#Execute window
window.mainloop()