# Personal Finance Tracker

A Personal Finance Tracker built using Tkinter to help users keep track of their daily expenses. This project provides a graphical user interface (GUI) for recording expenses along with their categories and dates. 

## Features

- Expense Logging: Add expense amounts, categories, and dates easily in the interface.
- Validation: Ensures all fields are filled before adding an expense.
- Dynamic Feedback: Displays success or error messages directly within the app. 
- File Saving: Expenses are saved in a CSV file, which allows for data retention even after closing the app.
- Total Expense Calcultion: Calculates and displays the total expense at the bottom of the window and CSV file, updated every time a new expense is added.
- Category Filter: Display expenses based on category by selecting the category in the drop-down menu and clicking the filter button.
- Delete Expense: Delete expense if needed (Misinput, Duplicates, etc)

## Challenges Faced

- User input validation: Ensure that the user enter the correct date and expenses to avoid error. This was overcome by having an amount and date validation. The amount valition will throw an error message if user inputs a negative number. The date validation uses the datetime.strptime() function to ensure the date format is YYYY-MM-DD.
- GUI Layout: Designing a user-friendly interface in Tkinter while ensuring proper alignment and readibility. This was overcome by using padding (pady) and widget placement (pack()) to maintain a structured layout. Different font, sizes and colors were also experimented for best visibility.
- Dynamic Label: It was challenging to display accurate data of total expenses every time a change has been made. This was overcome by implementing a refresh_total_label function to update the label in real time everytime a change was made.
