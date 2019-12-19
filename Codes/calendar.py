# Importing the calendar library.
import calendar

# Printing all months in a year.
for name in calendar.month_name:
    print(name)

# TextCalendar class can be used to generate plain text calendars.
c = calendar.TextCalendar(calendar.SUNDAY)

# TextCalendar instances has the following method:
s = c.formatmonth(2019, 12, 0, 0)
# Return a month’s calendar in a multi-line string. If w is provided, it specifies the width of the date columns, which are centered. If l is given, it specifies the number of lines that each week will use.

print(s)

# HTMLCalendar is used to print in HTML format.
hc = calendar.HTMLCalendar(calendar.SUNDAY)
s = hc.formatmonth(2019, 12)

print(s)

# We can print the days as well as the dates in a particular month by iterating through the object.
for i in c.itermonthdays(2019, 12):
    print(i)
# itermonthdates() will return the dates in a particular month in a year.
