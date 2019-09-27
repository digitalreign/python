# 20190925 BeginningPython Chapter 5
# Conditional, Loops, and Some Other Statements

# 20190925 page 71
# Printing Multiple Arguments

print('Month:', 'January')
month = 'January'
year = '2019'
day = '01'
print(day, month, year)
# 20190927 page 71 more printing arguements
print("Adding comma after the month")
print(day, month + ',', year)
print("Adding seperator instead of space:")
print(day, month, year, sep="_")

# Importing Something as Something Else
import math as notmath
print(notmath.sqrt(4))
from math import sqrt as notsqrt
print(notsqrt(9))