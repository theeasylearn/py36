#write a program to findout which brother is elder(older) brother from 2 brother age given by user. 
age_1 = int(input("enter 1st brother age"))
age_2 = int(input("enter 2nd brother age"))

if age_1>age_2: #< > <= >= == !=
    print("1st brother is elder brother")

if age_1<age_2:
    print("2nd brother is elder brother")

if age_1==age_2:
    print("both brothers are of same age")

print("good bye....")
