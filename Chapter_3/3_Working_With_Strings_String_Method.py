# 20190828 BeginningPython Chapter 3
# Working with Strings

# 20190828 page 52
# String Method

# Center
print("Monday, Tuesday, Wednesday".center(39))
print("Thursday, Friday Saturday".center(39, "*"))

# Find
print("Monday, Tuesday, Wednesday".find('day'))
day = "Thursday, Friday Saturday"
print(day.find('Thursday'))
print(day.find('Friday'))
print(day.find('Saturday'))
print(day.find('Sunday'))

# 20190831 Join
dirs = '', 'usr', 'bin', 'env'
'/'.join(dirs)
print('C:' + '\\'.join(dirs))

# Lower
print('Thursday, Friday, Saturday'.lower())
if 'Friday' in (day): print('Found The Friday!')
if 'friday' in (day): print('Found The friday!')
