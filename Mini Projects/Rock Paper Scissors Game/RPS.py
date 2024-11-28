import random

choice = ["rock","paper","scissors"]
win = "You win!"
lose = "You lose!"

def RPS_game():
    while True:
        move = input("Rock, Paper, or Scissors").lower()
        if move in choice:  #prompt user for input until user input one of the choices
            break
        else:
            print("Please enter a valid move")
         
    opponent = random.choice(choice) #assign a random choice in the list to opponent
    print(f"Opponent Move: {opponent}")
    
    if move == opponent:
        return "Tie"
    elif (move == "rock" and opponent == "scissors") or \
         (move == "paper" and opponent == "rock") or \
         (move == "scissors" and opponent == "paper"):
        return "Win"
    else:
        return "Lose"

print(RPS_game())

while input("Do you want to play again? (y/n): ").lower() == "y": #ask user if they want to play again
    print(RPS_game())
else:
    print("Thanks for playing!")
