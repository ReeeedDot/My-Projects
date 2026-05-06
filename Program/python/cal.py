import calendar
year = 2024
month =2

  #generate the calendar for the specified ear and month
cal = calendar.monthcalendar(year,month)

  #print the calendar
print(calendar.month_name[month],year)
print("Mo Tu We Th Fr Sa Su")
for week in cal:
      print("".join(str( day)if day !=0 else" " for day in week))