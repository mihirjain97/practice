import datetime
import pytz


todayDate = datetime.date.today()
print(todayDate)
birthday = datetime.date(1997, 5, 15)
print(birthday)

print(repr(birthday))

days_since_birth = (todayDate - birthday).days

print(days_since_birth)

tdelta = datetime.timedelta(days=365)

print(todayDate - tdelta)

print(todayDate.month)

# Monday = 0 - Sunday = 6
print(todayDate.weekday())

print(datetime.time(23, 25, 30, 512346))
#datetime.date(Y, M, D)
#datetime.time(h, m, s, ms)
#datetime.datetime(Y, M, D, h, m, s, ms)

# add 10hours to curent time
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

# TimeZones
dateTime_today = datetime.datetime.now(tz=pytz.UTC)
dateTime_India = dateTime_today.astimezone(pytz.timezone('Asia/Kolkata'))
print(dateTime_India)

# for tz in pytz.all_timezones:
#     print(tz)


# string formatting
# 2020-08-25 -> August 25, 2020
# strftime(f=formatting)
dateTime_Format = dateTime_India.strftime('%B %d, %Y')
print(dateTime_Format)

# August 25, 2020 -> datetime(2020, 08, 25)
# strptime(p=parsing)

dateTime_Parsing = datetime.datetime.strptime('August 25, 2020', '%B %d, %Y')
print(repr(dateTime_Parsing))
