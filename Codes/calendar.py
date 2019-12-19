import calendar

# TextCalendar class can be used to generate plain text calendars.
c = calendar.TextCalendar(calendar.SUNDAY)

# TextCalendar instances has the following method:
s = c.formatmonth(2019, 12, 0, 0)
# Return a month’s calendar in a multi-line string. If w is provided, it specifies the width of the date columns, which are centered. If l is given, it specifies the number of lines that each week will use.

print(s)
