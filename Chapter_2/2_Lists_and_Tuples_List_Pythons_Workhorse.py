# 20190818 BeginningPython Chapter 2 

# 20190818 page 34
# List's: Python's Workhorse

# The List function
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
print(list('Months'))

# Changing lists
print(months)
months[1] = 'Joseuary'
print(months)

# 20190818 page 35 Deleting Elements
del months[2]
print(months)

# Assigning to slices
capital = list('Months')
print (capital)
# Change letters to capitals
capital[2:] = list('NTHS')
print (capital)
# Add ly
capital[5:] = list('ly')
print (capital)
