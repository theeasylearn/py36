import datetime # date time module 

# from datetime import datetime as dt
# date = dt.now()

date = datetime.datetime.now() # module.class.method
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

today = weeks[date.weekday()] + " " + str(date.day) + "/" + str(date.month) + "/" + str(date.year)

currentTime = str(date.hour) + ':' + str(date.minute) + ":" + str(date.second)

print(today)
print(currentTime)