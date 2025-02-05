from tkinter import *

#Create window
window = Tk()

#Configure Window settings
window.title("Hello World")
window.geometry('350x200')

def reset():
    txt.delete(0,END)
    lbl.configure(text = "Test Words for input")

#Menu bar
menu_bar = Menu(window)

#create menu
menu_1 = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=menu_1)
menu_1.add_command(label='New', command=reset)
menu_1.add_separator()
menu_1.add_command(label='Exit',command=window.quit)
window.config(menu=menu_bar)

#Window Content
lbl = Label(window, text="Test Words for input")
lbl.grid()

#Entry Field
txt = Entry(window, width=10)
txt.grid(column=1, row=0)

#funciton for buttons
def clicked():
    result = "You wrote: " + txt.get()
    lbl.configure(text = result)

#Configure button
btn = Button(window, text = "Click Here",
             fg = "red", command=clicked)

#Configure Reset
btn_reset = Button(window, text = "Reset",
             fg = "Black", command=reset)

#Set buttons to grid
btn.grid (column=2, row=0)
btn_reset.grid (column=3, row=0)

#Execute window
window.mainloop()