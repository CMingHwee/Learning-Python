#Find the longest word in the sentence

text = input("Please enter a sentence: ) #Takes input from user

def longest_word(text):
    x = text.split()     #split the words in the sentence into a list of word
    longest = ""         #empty variable to store longest word
    
    for word in x:
        if len(word) > len(longest):  #check if length of current word is longer than the length of the word in "longest" variable
            longest = word            #if current word is longer, replace the word in "longest" variable
    return(longest)
print("The longest word in the sentence is: ", longest_word(text)) #output of longest word
