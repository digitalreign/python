# 20190906 BeginningPython Chapter 4
# Dictionaries: When Indices Won’t Do

# 20190906 page 62
# A simple database

# A dictionary with person names as keys. Each person is represented as
# another dictionary with the keys 'phone' and 'addr' referring to their phone
# number and address, respectively.
people = {
    'January': {
        'phone': '555-3131',
        'addr': '31 January Way'
    },
    'February': {
        'phone': '555-2828',
        'addr': '28 February Drive'
    },
    'April': {
        'phone': '555-3030',
        'addr': '30 April Street'
    }
}
# Descriptive labels for the phone number and address. These will be used
# when printing the output.
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')
# Are we looking for a phone number or an address?
request = input('Phone number (p) or address (a)? ')
# Use the correct key:
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# Only try to print information if the name is a valid key in
# our dictionary:
if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
else: print('Name not found.')

# 20190907 String Formatting with Dictionaries page 63
zipcode = {'January': '010101', 'February': '020202', 'April': '040404'}
print("January's zipcode is {January}.".format_map(zipcode))

# clear page 64
clear = {}
clear['name'] = 'January'
clear['age'] = 42
print(clear)
returned_value = clear.clear()
print(clear)
print(returned_value)

# 20190909 copy page 64
Seasons = {'Season': 'Spring', 'Months': ['March', 'April', 'May']}
print('The Old Seasons')
print(Seasons)
New_Seasons = Seasons.copy()
New_Seasons['Season'] = 'Summer'
New_Seasons['Months'].remove('March')
print('The New Seasons')
print(New_Seasons)

# 20190910 fromkeys page 65-66
{}.fromkeys(['day', 'appointments'])
week = {}
print('Should return None')
print(week.get('day'))