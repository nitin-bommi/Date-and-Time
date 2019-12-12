#Importing date class from datetime module
from datetime import date

today_date = date.today()

#Printing the date in YYYY-MM-DD format
print(today_date)

#Particular year, month, date can be accessed by using date, month, year methods from today_date.

#We can even declare date to a particular variable and perform operations on that variable.
christmas = date(today_date.year, 12, 25)

if today_date>christmas:
	print("It's been %d days since Christmas passed this year" % ((today_date-christmas).days))
else:
	print("%d days more for Christmas 🥳" % ((christmas-today_date).days))
