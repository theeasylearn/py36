# Write a program to calculate multiplication of Numbers from 1 to n
# n = 3 // 3 * 2 * 1 = 6

def calculateMulti(n):
    if n == 1:
        return 1
    else:
        return n * calculateMulti(n-1)


number = int(input("Enter a number: "))
print(calculateMulti(number))