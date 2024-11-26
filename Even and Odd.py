#Create a list of even and odd numbers from another 
list1 = [1,2,3,4,5,6]
even = [] #empty list to store even numbers
odd = []  #odd list to store odd numbers

for x in list1:
    if x%2==0:
        even.append(x) #append x to even list if x is even
    else:
        odd.append(x) #append x to odd list if x is odd
print(f"The even numbers are {even}")
print(f"The odd numbers are {odd}")
