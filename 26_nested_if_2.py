#write a program to accept batter run from user. if runs are above or equal to 100, congratulate batter other wise ask batsman to improve cricketing skill 
runs = int(input("Enter batter's run"))
if runs<0:
    print("invalid run, run must be >=0")
else:
    if runs>=100:
        print("congratulation, you have made century.")
    else:
        print("ohh, you should have scored century")
print("good bye")