from tkinter import *

window = Tk() #instantiate an instance of window
window.title("Personal Fiance Tracker") #title of the window
window.geometry("420x420") #set window size


# Create a label and entry field for the expense amount
label = Label(window, text="Expense Amount: ")
label.pack()  # Add the label to the window
expense = Entry(window)  # Create an entry field for the user to input the expense amount
expense.pack()  # Add the entry field to the window

label2 = Label(window,
              text = "Category: ")
label2.pack()
category = Entry(window)
category.pack()

label3 = Label(window, 
               text="Date (YYYY-MM-DD):")
label3.pack()
date = Entry(window)
date.pack()
