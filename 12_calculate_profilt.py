# write a program to calculate profit amount of using given product purchase price and profit rate
#input 
purchase_price = int(input("Enter purchase price"))
profit_rate = float(input("Enter profit rate"))

#process 
sales_price = purchase_price + (purchase_price * profit_rate) / 100
print(f"Sales price = {sales_price}")
