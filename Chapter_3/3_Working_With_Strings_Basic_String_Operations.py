# 20190823 BeginningPython Chapter 3
# Working with Strings

# 20190823 page 45
# String Formatting
format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)

from string import Template
tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(who="Mars", what="Dusty"))

# Creating a list then manipulating it.
print("{}, {}, {}, {}, {}, {} and {}".format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
print("{1}, {3}, {5}, {0}, {2}, {4} and {6}".format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))

# 20190823 page 46
# Grabbing values and inputting them into a statement.
from math import pi
print("{name} is approximately {value:.2f}.".format(value=pi, name="π"))
print("{name} is approximately {value}.".format(value=pi, name="π"))