#write a program to calculate and display compound interest of given amount rate year
amount = int(input("Enter amount"))
rate = float(input("Enter rate"))
year = int(input("Enter year"))
count = 1
original_amount = amount 
while count<=year:
    interest = (amount * rate * 1) /100
    amount = amount + interest
    count = count + 1 

compound_interest = amount - original_amount
print("Compound Interest ", compound_interest)
