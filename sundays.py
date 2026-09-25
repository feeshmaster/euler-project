import calendar

year = 1901
max_year = 2000

count = 0

for yr in range(year, max_year + 1):
    for month in range(1, 13):
        for day in calendar.Calendar().itermonthdates(yr, month):
            if day.year == yr and day.month == month and day.day == 1:
                if day.strftime("%A") == "Sunday":
                    count += 1

print(count)
