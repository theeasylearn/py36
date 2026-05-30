#write a program to make sum of all digits in given amount 
# amount = 12345
# amount = 1 + 2 + 3 + 4 + 5 = 15
#output 
amount = int(input("Enter amount"))
total = 0

while amount>0:
    reminder = amount % 10
    total = total + reminder
    amount = amount // 10 # 1234

print(total)
