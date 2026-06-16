# write a program to create function that convert & return given fahrenheit into celsius 

def farenhitToCelcius(farenhit):
    celcius = (farenhit - 32) * (5/9)
    return celcius

f1 = float(input('Enter feranhit value'))
print("Celcius value is: ", farenhitToCelcius(f1))