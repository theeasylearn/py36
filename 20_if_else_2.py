# write a program to accept purchase price and sales price from user. findout profit or loss amount
purchase_price = int(input("Ente purchase price"))
sales_price = int(input("Enter sales price"))
difference = sales_price - purchase_price
if difference>0:
    print(f"you have made profit of {difference}")
else:
    print(f"you have made loss of {difference}")

print('good bye')