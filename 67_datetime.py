import datetime # date time module 

date = datetime.datetime.now() # module.class.method
weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print(weeks[date.weekday()] + ' ' + date.day)