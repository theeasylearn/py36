# import mymath
from mymath import getSquare, getQube

number = int(input('Enter a number: '))
print('Number is: ', number)

# print('Square of number is: ', mymath.getSquare(number))
# print('Qube of number is: ', mymath.getQube(number))

print('Square of number is: ', getSquare(number))
print('Qube of number is: ', getQube(number))