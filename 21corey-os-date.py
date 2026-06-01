import os
print(os.getcwd())

# Change the current working directory
os.chdir('C:\\Users\\home\\Desktop\\')

# Get the current working directory again to confirm the change
print(os.getcwd())


# Date
import datetime

d=datetime.date(2026, 5, 25)
print(d)

# Get the current date
current_date = datetime.date.today()
print(current_date)
print(current_date.weekday())  # Monday is 0 and Sunday is 6
print(current_date.isoweekday()) # Monday is 1 and Sunday is 7

print(dir(datetime.datetime))