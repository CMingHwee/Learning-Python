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
    
    if move == "rock" and opponent == "paper":
        print("opponent move: ", opponent)
        print(lose)
    elif move == "rock" and opponent == "scissors":
        print("opponent move: ", opponent)
        print(win)
    elif move == "paper" and opponent == "scissors":
        print("opponent move: ", opponent)
        print(lose)
    elif move == "paper" and opponent == "rock":
        print("opponent move: ", opponent)
        print(win)
    elif move == "scissors" and opponent == "rock":
        print("opponent move: ", opponent)
        print(lose)
    elif move == "scissors" and opponent == "paper":
        print("opponent move: ", opponent)
        print(win)
    elif move == opponent:
        print("opponent move: ", opponent)
        print("Tie!")
        

RPS_game()

while input("Do you want to play again? (y/n): ").lower() == "y": #ask user if they want to play again
    RPS_game()
else:
    print("Thanks for playing!")
