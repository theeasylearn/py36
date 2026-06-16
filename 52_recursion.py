# An example of a recursive function to find the factorial of a number
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def findFactorialOfNumber(number):
    if number == 1:
        return 1
    else:
        return number * findFactorialOfNumber(number - 1)

num = int(input('Enter a number'))
print("Factorial of number is: ", findFactorialOfNumber(num))    