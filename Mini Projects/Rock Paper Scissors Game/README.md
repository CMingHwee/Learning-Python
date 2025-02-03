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

## Challenges Faced 
- User input validation: The program will not read certain user's input due to case sensitivity (for example "Rock" , "rocK" or "ROCK"), I overcome this challenge by converting every input into lowercase, making the program case-insensitive. This avoids error no matter which variant the user types for their input. 
- Difficulty levels: Unsure how to make the game more challenging based on difficulty level, I decided to change the computer's behavior so that it adapts to user's past input and using that information to develop a counter-strategy, using the user's strategy against themselves. To achieve this, I adjust the weight of each move every time the user makes a move, making the computer more likely to use a move that will counter the user's most frequent choice. 