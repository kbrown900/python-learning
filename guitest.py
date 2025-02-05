from tkinter import *

#Create window
window = Tk()

#Configure Window settings
window.title("Hello World")
window.geometry('350x200')

def reset():
    txt.delete(0,END)
    lbl.configure(text = "Test Words for input")

def closeProgram():
    window.quit()

#Menu bar
menu_bar = Menu(window)

#create menu
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

#function for buttons
def clicked():
    result = "You wrote: " + txt.get()
    lbl.configure(text = result)

#Configure buttons
btn = Button(window, text = "Click Here",
             fg = "red", command=clicked)

btn_reset = Button(window, text = "Reset",
             fg = "Black", command=reset)

btn_close = Button(window, text='Close',
                   fg = "Black", command=closeProgram)

#Set buttons to grid
btn.grid (column=2, row=0)
btn_reset.grid (column=3, row=0)
btn_close.grid(column=6, row=1)

#Execute window
window.mainloop()