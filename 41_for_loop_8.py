#write a program to count vowels in given string (a,e,i,o,u)
text = input("What is your name")
count = 0
#use for loop on string 
vowels = ['a','e','i','o','u','A','E','I','O','U']
for letter in text:
    if letter in vowels:
        count = count + 1
print(f"\n count of vowels = {count}")
