balance = 2000  # global variable

def addMoney(amount): # amount is local variable
    global balance
    balance = balance + amount

print('Balance is: ', balance)
addMoney(500)
print('New balance is: ', balance)
