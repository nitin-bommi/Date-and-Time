#Importing the necessary class
from datetime import datetime

#Accessing a method from datetime to get both the date as well as the time
now = datetime.now()

#Printing the current date(YYYY-MM-DD) along with time(HH-MM-SS)
print(now)

#To get the year
print(now.year)

#To get the month
print(now.month)

#To get the day
print(now.day)
