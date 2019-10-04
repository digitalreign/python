# 20191002 BeginningPython Chapter 5
# Conditional, Loops, and Some Other Statements

# 20191002 page 76-77 Conditions and Conditional Statements

# True and False are just 1 and 0.
print('Should return 11:')
print(True + 10)
print('Should return True:')
print(bool('Something here'))

# 20191003 page 78 if and else clauses
name = input('What is your name? ')
if name.endswith('Reign'):
# 20191004 page 78-79 elif and Nesting Blocks
    if name.startswith('Mr.'):
        print('Hello Mr. Reign')
    elif name.startswith('Mrs.'):
        print('Hello Mrs. Reign')
    else:
        print('Hello, Reign')
else:
    print('Hello, Stranger')
status = "friend" if name.endswith("Reign") else "stranger"
print(status)
