import calendar

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021, 8, 3))
print()

print(calendar.monthcalendar(2021, 8))
print()

print(calendar.calendar(2022))
print()

day_of_the_week = calendar.weekday(2020, 8, 23)
print(day_of_the_week)

print()

leap_year = calendar.isleap(2020)
print(leap_year)

print()
leap_days = calendar.leapdays(2000, 2860)
print(leap_days)
