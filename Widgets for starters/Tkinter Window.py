from tkinter import *

from datetime import date

window = Tk()
window.geometry("500x500")
window.title("My first widget")

lb1 = Label(text= "Welcome", fg= "black", bg= "pink", height= 2, width= 100)
lb1.pack()
lb2 = Label(text= "Enter your Name", fg= "white", bg= "blue", height= 2)
lb2.pack()

input_name = Entry(width=40)
# Function to display a Message

def display():

    name = input_name.get()

    global message

    message = "Welcome to the Application! \nToday's date is: "

    greet = "Hello "+ name+"\n"

    text_box.insert(END, greet)

    text_box.insert(END, message)

    text_box.insert(END, date.today())
button = Button(text="click",fg="black", bg= "yellow", command= display)
text_box = Text(height=5)

input_name.pack()
button.pack()
text_box.pack()


window.mainloop()


