print("Months number checker")
month_count = [31,28,31,30,31,30,31,31,30,31,30,31]
calendar = {"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":"30","October":31,"November":30,"December":31}
year = int(input("Enter the Year: "))
leap_year = year%4
if leap_year == 0:
    calendar["February"] = 29
month = input("Enter month to get the no of days in it: ").title()
print(f" The given month {month} has {calendar[month]} days in the year {year}")


