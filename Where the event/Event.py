from tkinter import *

# Create window

window = Tk()

window.title("Event Handler")

window.geometry("200x200")



def click():

    print("\n The button is clicked")


button = Button(text="Click me!")

button.pack()

button.bind("<Button-1>",click)

window.mainloop()