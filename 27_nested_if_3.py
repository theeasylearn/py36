# write a program to findout given year is leap year or not 
year = int(input("Enter year"))

rem1 = year % 4
rem2 = year % 100
rem3 = year % 400

if rem1==0 and rem2!=0:
    print("this is leap year")
else:
    if rem2==0 and rem3==0:
        print("it is leap year")
    else:
        print("it is not leap year")


