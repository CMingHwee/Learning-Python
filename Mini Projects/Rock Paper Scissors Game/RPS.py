import random

move_history = [] #empty list to track move history
choice = ["rock","paper","scissors"]
wins, losses, ties = 0,0,0 #user win lose tie record starts at 0
p_rock , p_paper, p_scissors = 0.33, 0.33, 0.33 #probability of each move bring thrown

def RPS_game():
    global wins, losses, ties
    global p_rock, p_paper, p_scissors

    while True:
        move = input("Rock, Paper, or Scissors").lower()
        if move in choice:  #prompt user for input until user input one of the choices
            move_history.append(move) #add move to move history
            if len(move_history) > 10:
                move_history.pop(0) #move history caps at 10
            break
        else:
            print("Please enter a valid move")
    most_used = max(move_history, key= move_history.count) #store the most used move in move history
    if most_used == "rock":
        p_paper += 0.1 #increase probability of ai throwing paper if user's most used move is rock
        p_rock -= 0.05 #decrease probability of other moves to make up for the increased probability of paper
        p_scissors -= 0.05
    elif most_used == "paper":
        p_scissors += 0.1
        p_rock -= 0.05
        p_paper -= 0.05
    elif most_used == "scissors":
        p_rock += 0.1
        p_paper -= 0.05
        p_scissors -= 0.05
            
    p_rock = max(0, min(1, p_rock)) #ensure the probability of each move does not go negative or exceed 1
    p_paper = max(0, min(1, p_paper))
    p_scissors = max(0, min(1, p_scissors))
  
    opponent = random.choices(choice, weights =[p_rock, p_paper, p_scissors]) #assign a random choice in the list to opponent, with the ability to throw out moves based on user's behavior
    print(f"Opponent Move: {opponent[0]}")
   
    
    if move == opponent[0]:
        ties+=1
        print("It's a Tie!")
    elif (move == "rock" and opponent[0] == "scissors") or \
         (move == "paper" and opponent[0] == "rock") or \
         (move == "scissors" and opponent[0] == "paper"):
        wins+=1
        print("You Win!")
    else:
        losses+=1
        print("You Lose!")
    print(f"Score: Win: {wins} Lose: {losses} Tie: {ties}")   

RPS_game()

while input("Do you want to play again? (y/n): ").lower() == "y": #ask user if they want to play again
    RPS_game()
else:
    print(f"Final score: Win {wins} Lose: {losses} Tie: {ties}")
    print("Thanks for playing!")




