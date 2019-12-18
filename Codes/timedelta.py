# With timedelta objects, you can estimate the time for both future and the past.

# Importing the timdelta class from datetime module.
from datetime import timedelta

# construct a basic timedelta and print it
print (timedelta(days=365, hours=8, minutes=15))

# print today's date
print ("today is: " + str(datetime.now()))

# print today's date one year from now
print ("one year from now it will be:" + str(datetime.now() + timedelta(days=365)))

# create a timedelta that uses more than one argument
# print (in one week and 4 days it will be " + str(datetime.now() + timedelta(weeks=1, days=4)))
# How many days until New Year's Day?
today = date.today()  # get todays date
nyd = date(today.year, 1, 1)  # get New Year Day for the same year
# use date comparison to see if New Year Day has already gone for this year
# if it has, use the replace() function to get the date for next year
if nyd < today:
    print ("New Year day is already went by %d days ago" % ((today - nyd).days))
    
