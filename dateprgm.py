year = input("year:")
month = input("month(1-12):")
day = input("day(1-31): ")
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
'September', 'October', 'Novermber', 'December']
monthIndex = int(month) 1
monthOutput = months [monthIndex]
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
dayIndex = int(day) - 1
dayOutput = day + endings [dayIndex]
print(endings)
print( monthOutput + + dayOutput + "," + year)
