from tkinter import *

#Create window
window = Tk()

#Configure Window settings
window.title("Hello World")
window.geometry('350x200')

#Window Content
lbl = Label(window, text="Test Words")
lbl.grid()

#funciton for button
def clicked():
    lbl.configure(text = "Button Clicked")

#Configure button
btn = Button(window, text = "Click Here",
             fg = "red", command=clicked)

#Set button to grid
btn.grid (column=1, row=0)


#Execute window
window.mainloop()