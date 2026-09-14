# pylint: disable=redefined-outer-name, reimported, wildcard-import, unused-wildcard-import, redefined-builtin, invalid-name

# Python Functions
# Example: Python Function Call
def greet():
    print('Bonjour le monde!')

# call the function
greet()

print('Outside function')


# Python Function Arguments
def greet_with_name(name):
    print("Bonjour", name)

# pass argument
greet_with_name("Han")


# Example: Function to Add Two Numbers
# function with two arguments
def add_numbers(num1, num2):
    total = num1 + num2
    print("Sum: ", total)

# function call with two values
add_numbers(3, 7)


# The return Statement
# function definition
def find_square(number):
    result = number * number
    return result

# function call
square = find_square(9)

print('Square:', square)


# The pass Statement
def future_function():
    pass

# this will execute without any action or error
future_function()


# Example: Python Library Function
import math

# sqrt computes the square root
square_root = math.sqrt(9)

print("Square Root of 9 is", square_root)

# pow() computes the power
power = pow(4, 5)

print("4 to the power 5 is", power)


# Python Function Arguments
# Example 1: Python Function Arguments
def add_numbers_simple(a, b):
    total = a + b
    print('Sum:', total)

add_numbers_simple(3, 7)

# Output: Sum: 10


# Function Argument with Default Values
def add_numbers_defaults(a=6, b=2):
    total = a + b
    print('Sum:', total)


# function call with two arguments
add_numbers_defaults(5, 3)

# function call with one argument
add_numbers_defaults(a=5)

# function call with no arguments
add_numbers_defaults()


# Python Keyword Argument
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name='Han', first_name='Taesan')


# Python Function With Arbitrary Arguments
# program to find sum of multiple numbers

def find_sum(*numbers):
    result = 0

    for number in numbers:
        result = result + number

    print("Sum = ", result)

# function call with 3 arguments
find_sum(4, 5, 6)

# function call with 2 arguments
find_sum(8, 9)


# Python Variable Scope
# Python Local Variables
def greet_local():

    # local variable
    message = 'Bonjour'

    print('Local', message)

greet_local()

# try to access message variable
# outside greet() function
# print(message)


# Python Global Variables
# declare global variable
global_message = 'Bonjour'

def greet_global():
    # declare local variable
    print('Local', global_message)

greet_global()
print('Global', global_message)


# Python Nonlocal Variables
# outside function
def outer():
    outer_message = 'local'

    # nested function
    def inner():

        # declare nonlocal variable
        nonlocal outer_message

        outer_message = 'nonlocal'
        print("inner:", outer_message)

    inner()
    print("outer:", outer_message)

outer()


# Python Global Keyword
# Access and Modify Python Global Variable
c = 1 # global variable

def add():
    print(c)

add()

# Output: 1


# global variable
c = 1

def add_pass():

    # increment c by 2
    # c = c + 2
    # print(c)
    pass

# add_pass()


# Example: Updating a value from inside a function without using global
# global variable
c = 1

def add_global(value):

    # increment value by 2
    value = value + 2

    print(value)
    return value

c = add_global(c)

# Output: 3


# Python Recursion
# Example of a recursive function
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


# Python Modules
# Import Python Standard Library Modules
# math was already imported at the top of this file
# use math.pi to get value of pi
print("The value of pi is", math.pi)


# Python import with Renaming
# create a shorter alias for the already imported module
m = math

print(m.pi)

# Output: 3.141592653589793


# Python from...import statement
# import only pi from math module
from math import pi

print(pi)

# Output: 3.141592653589793


# Import only the names you need
# use a specific function or constant instead of wildcard import
print("The value of pi is", pi)


# Python Main function
# Running Python File as a Script
print(__name__)

# Using if conditional with __name__
def main():
    print("Bonjour le monde")

if __name__ == "__main__":
    main()