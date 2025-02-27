#Calories Tracker

weight = int(input("Please enter your weight in kg: "))
height = int(input("Please enter your height in cm: "))
age = int(input("Please enter your age: "))


activity = input("What is your activity level? \n 1.Sedentary \n 2.Lightly Active \n 3.Moderately Active \n 4.Very Active \n 5.Extremely Active: \n")
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
    
print(f"Your today daily energy expenditure is: {TDEE:.2f} \n")
total_calories_consumed = 0

while True:
    print("\nEnter food nutrients information")
    Carbohydrate = int(input("Please enter the Carbohydrate amount: ")) 
    Fat = int(input("Please enter the Fat amount: "))
    Protein = int(input("Please enter the Protein amount: "))
    Calories = ((Carbohydrate * 4) + (Fat * 9) + (Protein * 4))
    total_calories_consumed += Calories
    print(f"Nutrition Information: \nCarbohydrates: {Carbohydrate}g \nFats: {Fat}g \nProtein: {Protein}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < 0:
        print("You have exceeded your daily calorie intake!")
        break
