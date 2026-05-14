# write a program to calculate simple interest of given amount, rate, year 
#  si = (P X R X N) / 100

#input 
amount = int(input("Enter amount"))
rate = float(input("Enter rate"))
year = float(input("Enter year"))

#process 
simple_interest = (amount * rate * year) / 100

#display
print(f"Simple interest = {simple_interest}")
