import datetime

today = datetime.date.today()
# today_year = today[:5]

print(today)
print(type(today))
a = today.strftime('%Y/%m/%d')

year = '%s' % (today.year)
month = '%s' % (today.month)
day = '%s' % (today.day)

print(a)

print(year + " Year " + month + " Month " + day + " Day")
