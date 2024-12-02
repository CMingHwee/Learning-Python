from tkinter import *

window = Tk() #instantiate an instance of window
window.title("Personal Fiance Tracker") #title of the window
window.geometry("420x420") #set window size


#create a label and entry field for the expense amount
label = Label(window, 
              text ="Expense Amount: ")
label.pack()  #add the label to the window
expense = Entry(window)  #create an entry field for the user to input the expense amount
expense.pack()  #add the entry field to the window

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

def add_expense():  

#get data from their respective field
amount = expense.get() 
cat = category.get() 
date_data = date.get() 

if amount and cat and date_data: #validation to check if fields are filled
    print(f"Expense of ${amount} added under the category, {cat}, on {date_data}")
    #clear the entry fields after adding expense
    expense.delete(0, END) 
    category.delete(0, END)
    date.delete(0, END)
    
else:
    print("Please fill up all fields") #display error message if any field are empty
    
add_button = Button(window, text="Add Expense", command=add_expense) #create button for adding expense
add_button.pack() #add button to window

window.mainloop() #keep the window running so that it will not close after adding expense