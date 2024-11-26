#Calculate Tax, for every $ above $10,000, 10%
#increases to 20% for every $ above $20,000
amount = int(input("Enter an amount: "))

def calculate_tax(amount):
    if amount <= 10000:
        tax = 0
    elif amount <= 20000:
        tax = (amount - 10000) * 0.1 #10% tax
    else:
        tax = (amount - 20000) * 0.2 + (10000 * 0.1) #20% tax (above 20,000) + 10% tax (above 10,000 but below 20,000) 
    total = amount + tax
    print(f"Amount: ${amount}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

calculate_tax(amount)
