from tkinter import *
from tkinter import messagebox
from datetime import datetime
import os
import csv

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

total_label = Label(window,
                    text="Total Expense: $0.00")#label to display total expense
total_label.pack()  #add total expense label to window
              

def validate_date(date_text):
    #Check if the date is valid and follows YYYY-MM-DD format
    try:
        datetime.strptime(date_text, "%Y-%m-%d") #ensure date is in correct format
        return True
    except ValueError:
        return False

def save_file(amount,cat,date_data): #function to save data into csv
    file_name = "expenses.csv" #set file name
    file_exists = os.path.exists(file_name) #check if file exist
    try:
        with open(file_name, mode="a", newline="") as file: #open file in append mode
            writer = csv.writer(file) #create writer object
            if not file_exists:
              writer.writerow(["Amount","Category","Date"]) #write column headers first if file does not exist
            writer.writerow([f"{amount:.2f}",cat,date_data]) #write data into new row
    except Exception as e:
        messagebox.showerror("Save Error", f"An error has occurred while saving data: {e}") #display error details if data failed to save
              
def calculate_total_expense():  #function to calculate total expenses from CSV
    file_name = "expenses.csv" #file name to read
    total = 0.0 #initialize a variable to store total expense

    if os.path.exists(file_name): #check if file exist
        try:
            with open(file_name, mode="r") as file: #open file in read mode
                reader = csv.reader(file) #create writer object
                next(reader)  #skip header row so that it will not be included in the calculation
              
                for row in reader:
                    if row and row[0] != "Total Expense":  #check if row is not empty and doesn't have "Total Expense" label
                        total += float(row[0]) #convert value in "amount" row into float and add it to total
        except Exception as e:
            messagebox.showerror("Read Error", f"An error has occurred while reading the file: {e}") #display error if file failed to read
    return total

def write_total_to_csv():
    file_name = "expenses.csv"
    total_expense = calculate_total_expense() 
    try:
        rows = []
        if os.path.exists(file_name):
            with open(file_name, mode="r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)
              
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            total_row_exist = False 
              
            for row in rows:
                if row and row[0] == "Total Expense:":
                    #update the existing "Total Expense" row
                    writer.writerow(["Total Expense:", f"{total_expense:.2f}"])
                    total_row_exist = True
                else:
                    writer.writerow(row)
            
            #if the "Total Expense" row was not found, append it at the end
            if not total_row_exist:
                writer.writerow(["Total Expense:", f"{total_expense:.2f}"])
    except Exception as e:
        messagebox.showerror("Update Error", f"An error has occurred while updating total expense: {e}")
        
def add_expense():  

#get data from their respective field
amount = expense.get() 
cat = category.get() 
date_data = date.get() 

#check if amount or date field is empty
if not amount or not date_data: 
        messagebox.showerror("Input Error", "Please fill up all fields")
        return

try:
    amount = float(amount) #conver amount to float
    if amount <= 0: #if amount = 0 or negative
        raise ValueError("Amount must be positive")
except ValueError: #if amount entered is something else like "abc"
    messagebox.showerror("Input Error", "Please enter a valid positive number for expense amount")
    return

if not validate_date(date_data): #check if date is in correct format
    messagebox.showerror("Input Error", "Please enter a valid date in the format YYYY-MM-DD")
    return

save_file(amount, cat, date_data)

total_expense = calculate_total_expense() #store total expense in total_expense
total_label.config(text=f"Total Expense: ${total_expense:.2f}") #label to display total expense

write_total_to_csv() #write total expense to csv

output_label.config(text=f"Expense of ${amount:.2f} added under the category, {cat}, on {date_data}", fg="green") #display message in green when success

#clear the entry fields after adding expense
expense.delete(0, END) 
date.delete(0, END)
    
add_button = Button(window, text="Add Expense", command=add_expense) #create button for adding expense
add_button.pack() #add button to window


window.mainloop() #keep the window running so that it will not close after adding expense