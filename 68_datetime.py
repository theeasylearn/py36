import datetime

date = datetime.datetime

birthdate = '27/12/2022'
print(birthdate)

date1 = date.strptime(birthdate, "%d/%m/%Y")
print(date1)

print(date.strftime(date1, "%Y/%m/%d"))