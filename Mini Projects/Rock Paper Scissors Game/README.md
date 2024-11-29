# Rock Paper Scissors Game

A simple implementation of the Rock, Paper, Scissors game in Python. 
The player competes against the computer, with the game determining the winner based on the choices made.
Computer will get stronger based on user's past moves, making it more challenging and engaging!
Multiple difficulty level to choose from!

## Features
- User inputs their choice (rock, paper, or scissors).
- Computer will adapt to user's past behavior (move history tracking) and changes its strategy.
- Score record of Win, Lose, and Tie during the game session will be displayed.
- The game determines the winner or if there's a tie.
- Option to play multiple rounds.
- Computer takes a moment to "think" before making its move, simulating a more lifelike opponent.
- Multiple difficulty levels:
     - Easy: Computer will make moves randomly without strategy
     - Medium: Computer will adapt by increasing the likelihood of countering user's most frequently used move
     - Hard: Computer will adapt more aggresively, significantly boosting the chances of selecting moves that counters the user's most frequently used move 