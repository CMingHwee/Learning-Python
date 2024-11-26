#Count number of repeated words in a sentence
sentence = "The roasted chicken rice made by Henry is the best chicken rice I have ever tasted!"

word = input("Enter a word to count: ")  #user enter word to be counted
count = 0   #count starts at 0

for x in sentence.split():       #split sentence into a list of words to loop through
  if x.lower() == word.lower():  #convert both word into lowercase so that it will be counted without being case-sensitive
    count+=1  #count increases for every repeated word
    
if count > 0: #if word exists
  print(f"The word '{word}' has appeared {count} times")
else:
  print(f"The word {word} does not exist in this sentence")
