#We can make use of formatted printing as in C.

# %y/%Y = Year
# %b/%B = Month
# %d = Day of the month
# %a/%A = Day of the week

from datetime import datetime

now = datetime.now()

# To print the year.
print(now.strftime("%Y"))
# Replacing Y with y will print only the last two digits of the year.

# Printing in default format.
print(now.strftime("Today :- %d %A, %B, %Y"))

# %C- indicates the local date and time
# %x- indicates the local date
# %X- indicates the local time

print(now.strftime("%c"))

# %I/%H - 12/24 Hour
# %M - minute
# %S - second
# %p - local's AM/PM

print(now.strftime("%I:%M:%S %p"))
