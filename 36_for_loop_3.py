#write a program to count odd and even numbers
#output : odd = 5
#output : even = 15
numbers = [14, 82, 45, 3, 67, 29, 91, 54, 8, 38, 71, 23, 60, 88, 12, 49, 95, 33, 76, 5, 42, 19, 84, 57, 66, 11, 73, 50, 27, 99]
odd = 0
even = 0
for num in numbers:
    reminder = num % 2
    if reminder == 0:
        even = even + 1
    else:
        odd = odd + 1

print("odd count = ",odd)
print("even count = ",even)