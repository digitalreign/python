# Beginning Python (From Novice to Professional)
# Chapter 2 Lists and Tuples

# Page 25 Sequence 20190811
edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
database = [edward, john]
print(database)

# Page 26 Common Sequence Operations 20190811
greeting = 'Hello'
print(greeting[0])
print(greeting[1])
print(greeting[2])
print(greeting[3])
print(greeting[4])
print(greeting[-1])

# Page 27 Calendar Indexing
months = [
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December'
]
# A list with one ending for each number from 1 to 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
+ ['st', 'nd', 'rd'] + 7 * ['th'] \
+ ['st']
year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')
month_number = int(month)
day_number = int(day)
# Remember to subtract 1 from month and day to get a correct index
month_name = months[month_number-1]
ordinal = day, endings[day_number-1]
# This is not pretty but it works for now, need to get rid of the extra ( ) and ''
print month_name, ordinal, year

# 20190812 Page 28 Slicing
tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30]
print tag[32:-4]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers [3:6]
print numbers [0:1]
print numbers [3:]
print numbers [:3]
print numbers [-3:]
print numbers [:-3]
