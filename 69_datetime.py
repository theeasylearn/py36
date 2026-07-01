import datetime

date = datetime.date
# day = int(input('Enter days '))
# month = int(input('Enter month '))
# year = int(input('enter year '))

# today = date(year, month, day)
# print(today)

d = input('Enter date in yyyy-mm-dd format ')
print(date.fromisoformat(d))