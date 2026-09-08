# Python Variables and Literals

# Assigning values to Variables in Python
# assign value to site_name variable
site_name = 'adios!.boynextdoor'

print(site_name)
print()

# Output: adios!.boynextdoor


site_name = 'adios!.boynextdoor'
print(site_name)
print()

# Changing the Value of a Variable in Python
# assigning a new value to site_name
site_name = 'serenade.boynextdoor'
print(site_name)
print()

# Example: Assigning multiple values to multiple variables
a, b, c = 4, 4.1, 'Hello'

print(a)  # prints 4
print(b)  # prints 4.1
print(c)  # prints Hello
print()

site1 = site2 = 'adios!.boynextdoor'

print(site1)  # prints adios!.boynextdoor
print(site2)  # prints adios!.boynextdoor
print()

# Python Type Conversion

# Example 1: Converting integer to float
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:", new_number)
print("Data Type:", type(new_number))
print()

# Example 2: Addition of string and integer Using Explicit Conversion
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:", type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:", type(num_string))

num_sum = num_integer + num_string

print("Sum:", num_sum)
print("Data type of num_sum:", type(num_sum))
print()

# Python Basic Input and Output

# Example 1: Python Print Statement
print('Give me money!')
print('i want to be rich guy!')
print()

# Example 2: Python print() with end Parameter
# print with end whitespace
print('Give me money!', end=' ')

print('i want to be rich guy!')
print()

# Example 3: Python print() with sep parameter
print('Have a nice day', 1945, 'See you soon!', sep='. ')
print()

# Example: Print Python Variables and Literals
number = -10.6

name = "Gue"

# print literals     
print(5)

# print variables
print(number)
print(name)
print()

# Example: Print Concatenated Strings
print('Gue ' + 'awesome.')
print()

#Output formatting
x = 2
y = 4

print('The value of x is {} and y is {}'.format(x, y))
print()

# Example: Python User Input
# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))
print()

# Python Operators
# Arithmetic operators
x = 10
y = 5
print('x + y = ', x + y)
print('x - y = ', x - y)
print('x * y = ', x * y)
print('x / y = ', x / y)
print('x // y = ', x // y)
print('x ** y = ', x ** y)
print()

# Comparison operators
x = 10
y = 5
print('x > y  is', x > y)
print('x < y  is', x < y)
print('x == y is', x == y)
print('x != y is', x != y)
print('x >= y is', x >= y)
print('x <= y is', x <= y)
print()

# Logical operators
x = True
y = False
print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)
print()

# Bitwise operators
x1 = 5
y1 = 5
x2 = 'ola'
y2 = 'ola'
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)
print()

# Membership operators
x = 'Bonjour'
y = {1: 'a', 2: 'b'}
print('H' in x)
print('bonjour' not in x)
print(1 in y)
print('a' in y)