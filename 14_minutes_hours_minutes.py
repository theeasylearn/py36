#write a program to accept total minutes from user & then convert & display hours and remaining minutes
# input: 75 minutes 
# output : 1 hour & 15 minutes 

# input: 130 minutes 
#ouput : 2 hours & 10 minutes 

#input 
minutes = int(input("Enter minutes"))

#process 
hours = minutes // 60 # 1
minutes = minutes % 60 # 15

print(f"hours = {hours} minutes = {minutes}")
