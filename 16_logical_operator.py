#example of logical operator 

num1 = 10 
num2 = 20
num3 = 30
num4 = 40
print(f"num1 = {num1} num2 = {num2} num3 = {num3} num4 = {num4}")

result = num1 < num2 and  num3 < num4
print(f"{result} = {num1} < {num2} and {num3} < {num4}")

result = num1 < num2 and  num3 > num4
print(f"{result} = {num1} < {num2} and {num3} > {num4}")

result = num1 > num2 and  num3 > num4
print(f"{result} = {num1} > {num2} and {num3} > {num4}")

result = num1 < num2 or  num3 < num4
print(f"{result} = {num1} < {num2} or {num3} < {num4}")

result = num1 < num2 or  num3 > num4
print(f"{result} = {num1} < {num2} or {num3} > {num4}")

result = num1 > num2 or  num3 < num4
print(f"{result} = {num1} > {num2} or {num3} < {num4}")

result = num1 > num2 or  num3 > num4
print(f"{result} = {num1} > {num2} or {num3} > {num4}")

result = not (num1 > num2 or  num3 > num4)
print(f"{result} = not ({num1} > {num2} or {num3} > {num4})")