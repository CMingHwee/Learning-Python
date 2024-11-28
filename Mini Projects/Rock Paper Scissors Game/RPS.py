import random

choice = ["rock","paper","scissors"]
wins, losses, ties = 0,0,0 #scores to track

def RPS_game():
    global wins, losses, ties #set to global variable
    while True:
        move = input("Rock, Paper, or Scissors").lower()
        if move in choice:  #prompt user for input until user input one of the choices
            break
        else:
            print("Please enter a valid move")
         
    opponent = random.choice(choice) #assign a random choice in the list to opponent
    print(f"Opponent Move: {opponent}") #print out opponent move
    
    if move == opponent:
        ties+=1 #add 1 to the "tie" score 
        print("It's a Tie!")
    elif (move == "rock" and opponent == "scissors") or \
         (move == "paper" and opponent == "rock") or \
         (move == "scissors" and opponent == "paper"):
        wins+=1 #add 1 to the "wins" score
        print("You Win!")
    else:
        losses+=1 #add 1 to the "losses" score
        print("You Lose!")
    print(f"Score: Win: {wins} Lose: {losses} Tie: {ties}\n") #display current score

RPS_game()

while input("Do you want to play again? (y/n): ").lower() == "y": #ask user if they want to play again
    RPS_game()
else:
    print(f"Final score: Win {wins} Lose: {losses} Tie: {ties}") #display final score
    print("Thanks for playing!")
