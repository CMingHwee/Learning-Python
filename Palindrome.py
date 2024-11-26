#Check if the input is a palindrome
x = input("Enter a word or number: ")

def isPalindrome(x):
    if x.lower() == x[::-1].lower():  #ensure that the comparison is case-insensitive
        print("Original: ",x)        #prints original
        print("Reversed: ",x[::-1])  #prints reversed
        print(f"Yes, {x} is a palindrome.")
    else:
        print("Original: ",x)
        print("Reversed: ",x[::-1])
        print(f"No, {x} is not a palindrome.")
        
isPalindrome(x)
