# write a program to convert given fahrenheit into celsius
# Celsius = (Fahrenheit - 32) * 5 / 9. 

#input 
fahrenheit = input("Enter Fahrenheit")

#process 
fahrenheit = float(fahrenheit)
celsius = (fahrenheit - 32) * (5/9)
print(f"celsius = {celsius:.2f}")
