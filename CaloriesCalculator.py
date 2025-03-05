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

BMI = weight/((height/100)*(height/100))
print(f"\nYour BMI is {BMI:.1f}")

if BMI < 18.5:
    classification = "underweight"
    print("You are underweight.\n")
elif BMI <= 24.9:
    classification = "normal"
    print("You are healthy!\n")
elif BMI <= 30:
    classification = "overweight"
    print("You are overweight.\n")
elif BMI >= 30:
    classification = "obese"
    print("You are obese.\n")


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

print(f"\nYour total daily energy expenditure is: {TDEE:.2f} \n")
total_calories_consumed = 0

while True:
    if classification == "underweight":
        goal = input("\nWhat is your goal? (e.g. 1, 2, 3)\n 1. Weight Loss\n 2. Bulk (Recommended)\n 3. Body Recomposition\n")
    elif classification == "normal":
         goal = input("\nWhat is your goal? (e.g. 1, 2, 3)\n 1. Weight Loss\n 2. Bulk\n 3. Body Recomposition (Recommended)\n")
    elif classification == "overweight":
         goal = input("\nWhat is your goal? (e.g. 1, 2, 3)\n 1. Weight Loss (Recommended)\n 2. Bulk\n 3. Body Recomposition\n")
    elif classification == "obese":
         goal = input("\nWhat is your goal? (e.g. 1, 2, 3)\n 1. Weight Loss (Recommended)\n 2. Bulk\n 3. Body Recomposition\n")

    if goal in ["1", "2", "3"]:
        break
    else:
        print("Please enter a valid goal. (e.g., 1, 2, 3)\n")


if goal == "1":
    print("\nThe recommended macronutrient for weight loss is 30% Protein, 30% Fat, and 40% Carbs. Please try to stay within a 500 calorie deficit!")
elif goal == "2":
    print("\nThe recommended macronutrient for bulking is 30% Protein, 25% Fat, and 45% Carbs. Please try to stay within a 300 calorie surplus!")
elif goal == "3":
    print("\nThe recommended macronutrient for body recomposition is 35% Protein, 25% Fat, and 40% Carbs. Please try to stay within your calorie maintenance! (+- 300)")

        
total_protein = total_carb = total_fat = 0

print("\nEnter food nutrients information for Breakfast")
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
total_protein += Protein
total_carb += Carbohydrate
total_fat += Fat
total_calories_consumed += Calories
if goal == "1":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.4/4)}g \nFats: {total_fat}g/{round(TDEE*0.3/9)}g \nProtein: {total_protein}g/{round(TDEE*0.3/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < 0:
        print("You have exceeded your daily calorie intake!")
elif goal == "2":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.45/4)}g \nFats: {total_fat}g/{round(TDEE*0.25/9)}g \nProtein: {total_protein}g/{round(TDEE*0.3/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < -300:
        print("You have exceeded your daily calorie intake!")
elif goal == "3":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.4/4)}g \nFats: {total_fat}g/{round(TDEE*0.25/9)}g \nProtein: {total_protein}g/{round(TDEE*0.35/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < -300:
        print("You have exceeded your daily calorie intake!")
        
    

print("\nEnter food nutrients information for Lunch")
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
total_protein += Protein
total_carb += Carbohydrate
total_fat += Fat
total_calories_consumed += Calories
if goal == "1":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.4/4)}g \nFats: {total_fat}g/{round(TDEE*0.3/9)}g \nProtein: {total_protein}g/{round(TDEE*0.3/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < 0:
        print("You have exceeded your daily calorie intake!")
elif goal == "2":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.45/4)}g \nFats: {total_fat}g/{round(TDEE*0.25/9)}g \nProtein: {total_protein}g/{round(TDEE*0.3/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < -300:
        print("You have exceeded your daily calorie intake!")
elif goal == "3":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.4/4)}g \nFats: {total_fat}g/{round(TDEE*0.25/9)}g \nProtein: {total_protein}g/{round(TDEE*0.35/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < -300:
        print("You have exceeded your daily calorie intake!")
    

print("\nEnter food nutrients information for Dinner")
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
total_protein += Protein
total_carb += Carbohydrate
total_fat += Fat
total_calories_consumed += Calories

    
if goal == "1":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.4/4)}g \nFats: {total_fat}g/{round(TDEE*0.3/9)}g \nProtein: {total_protein}g/{round(TDEE*0.3/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < 0:
        print("You have exceeded your daily calorie intake!")
    elif Remaining <= 500:
        print("Good job staying within the recommended calorie deficit of 500!")
    else:
        print("You should be eating more!")
elif goal == "2":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.45/4)}g \nFats: {total_fat}g/{round(TDEE*0.25/9)}g \nProtein: {total_protein}g/{round(TDEE*0.3/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < -300:
        print("You have exceeded your daily calorie intake!")
    elif Remaining > 0:
        print("You should be eating more!")
    else:
        print("Good job staying within the recommended calorie surplus of 300!")
elif goal == "3":
    print(f"\nNutrition Information: \nCarbohydrates: {total_carb}g/{round(TDEE*0.4/4)}g \nFats: {total_fat}g/{round(TDEE*0.25/9)}g \nProtein: {total_protein}g/{round(TDEE*0.35/4)}g \nCalories: {Calories}kcal")
    Remaining = TDEE - total_calories_consumed
    print(f"Your calories left for the day is {Remaining:.2f} ")
    if Remaining < -300:
        print("You have exceeded your daily calorie intake!")
    elif Remaining > 300:
        print("You should be eating more!")
    else:
        print("Good job staying within the recommended calorie range!")







