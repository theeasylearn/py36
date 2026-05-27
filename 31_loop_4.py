# write a program to display following (series)
# 1 4 9 16 25 ..... 100
# 1 2 3 4  5 

number = 1
square = 0
while square<100:
    square = number * number
    print(square,end=' ')
    number = number + 1

