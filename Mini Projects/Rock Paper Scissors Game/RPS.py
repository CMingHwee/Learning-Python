#Calories Tracker
while True:
    try:    
        weight = int(input("\nPlease enter your weight in kg: "))
        if weight <= 0:
            print("Weight must be a positive number.")
        else:
            break
    except ValueError:
        print("Invalid Input. Please enter a number.")

while True:
    try:
        height = int(input("\nPlease enter your height in cm: "))
        if height <= 0:
            print("Height must be a positive number.")
        else:
            break
    except ValueError:
        print("Invalid Input. Please enter a number.")

while True:
    try:
        age = int(input("\nPlease enter your age: "))
        if age <= 0:
            print("Age must be a positive number.")
        else:
            break
    except ValueError:
        print("Invalid Input. Please enter a number.")


while True:
    activity = input("What is your activity level? (e.g., 1, 2, 3, 4, 5) \n 1.Sedentary \n 2.Lightly Active \n 3.Moderately Active \n 4.Very Active \n 5.Extremely Active: \n")
    
    if activity in ["1", "2", "3", "4", "5"]:
        break
    else:
        print("Please enter a valid level. (e.g., 1, 2, 3, 4, 5)\n")
        
BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

if activity == "1":
    TDEE = BMR * 1.2
if activity == "2":
    TDEE = BMR * 1.375
if activity == "3":
    TDEE = BMR * 1.55
if activity == "4":
    TDEE = BMR * 1.725
if activity == "5":
    TDEE = BMR * 1.9
    
print(f"Your total daily energy expenditure is: {TDEE:.2f} \n")
total_calories_consumed = 0

while True:
    print("\nEnter food nutrients information")
    while True:
        try:
            Carbohydrate = int(input("\nPlease enter the Carbohydrate amount in grams: "))
            if Carbohydrate < 0:
                print("Value cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    while True:
        try:
            Fat = int(input("\nPlease enter the Fat amount in grams: "))
            if Fat < 0:
                 print("Value cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
              print("Invalid input. Please enter a number.")

    while True:
        try: 
            Protein = int(input("\nPlease enter the Protein amount in grams: "))
            if Protein < 0:
                   print("Value cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
              print("Invalid input. Please enter a number.")
            
    Calories = ((Carbohydrate * 4) + (Fat * 9) + (Protein * 4))
    total_calories_consumed += Calories
    print(f"Nutrition Information: \nCarbohydrates: {Carbohydrate}g \nFats: {Fat}g \nProtein: {Protein}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < 0:
        print("You have exceeded your daily calorie intake!")
        break





