import datetime

print("Datetime examples:")
print(datetime.datetime.now())
print(datetime.date.today())
future= datetime.date.today() + datetime.timedelta(days=7)
print("Date after 7 days:",future)
print()