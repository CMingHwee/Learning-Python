#print out every number in a list that is divisible by user's input
number = int(input("Please enter a number: "))

list = [1,4,5,8,15,40,43]

def divisible(list):
  found = False
  for x in list:
    if x%number == 0:
      print(x)        #prints x if x is divisible by number
      found = True    #set found to True if x is divisible by number
      
  if not found:       #if found is False, print below
      print(f"There are no number divisible by {number}")
      
divisible(list)
