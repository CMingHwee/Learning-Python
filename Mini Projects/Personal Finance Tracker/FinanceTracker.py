from tkinter import *
from tkinter import messagebox
from datetime import datetime

window = Tk() #instantiate an instance of window
window.title("Personal Fiance Tracker") #title of the window
window.geometry("420x420") #set window size


#create a label and entry field for the expense amount
label = Label(window, 
              text ="Expense Amount: ")
label.pack()  #add the label to the window
expense = Entry(window)  #create an entry field for the user to input the expense amount
expense.pack()  #add the entry field to the window

categories = ["Food", "Transport", "Rent", "Entertainment", "Utilities", "Miscellaneous"] #categories list
label2 = Label(window,
              text = "Category: ") 
label2.pack()
category = StringVar(window)
category.set(categories[0]) #set default category to Food
category_dropdown = OptionMenu(window, category, *categories) #create dropdown menu
category_dropdown.pack()

label3 = Label(window, 
               text="Date (YYYY-MM-DD):")
label3.pack()
date = Entry(window)
date.pack()

output_label = Label(window,
                     text="")#label to display output in GUI instead of console
output_label.pack()

def validate_date(date_text):
    #Check if the date is valid and follows YYYY-MM-DD format
    try:
        datetime.strptime(date_text, "%Y-%m-%d") #ensure date is in correct format
        return True
    except ValueError:
        return False


def add_expense():  

#get data from their respective field
amount = expense.get() 
cat = category.get() 
date_data = date.get() 

#check if amount or date field is empty
if not amount or not date_data: 
        messagebox.showerror("Please fill up all fields")
        return

try:
    amount = float(amount) #conver amount to float
    if amount <= 0: #if amount = 0 or negative
        raise ValueError("Amount must be positive")
except ValueError: #if amount entered is something else like "abc"
    messagebox.showerror("Please enter a valid positive number for expense amount")
    return

if not validate_date(date_data): #check if date is in correct format
    messagebox.showerror("Please enter a valid date in the format YYYY-MM-DD")
    return


output_label.config(text=f"Expense of ${amount:.2f} added under the category, {cat}, on {date_data}", fg="green") #display message in green when success

#clear the entry fields after adding expense
expense.delete(0, END) 
date.delete(0, END)
    

    
add_button = Button(window, text="Add Expense", command=add_expense) #create button for adding expense
add_button.pack() #add button to window

window.mainloop() #keep the window running so that it will not close after adding expense