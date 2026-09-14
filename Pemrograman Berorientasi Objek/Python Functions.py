# Python Functions
# Example: Python Function Call
def greet():
    print('Bonjour Français!')

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
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)


# The return Statement
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)


# The pass Statement
def future_function():
    pass

# this will execute without any action or error
future_function()


# Example: Python Library Function
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is", square_root)

# pow() computes the power
power = pow(2, 3)

print("2 to the power 3 is", power)


# Python Function Arguments
# Example 1: Python Function Arguments
def add_numbers_simple(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers_simple(2, 3)

# Output: Sum: 5


# Function Argument with Default Values
def add_numbers_defaults(a=7, b=8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers_defaults(2, 3)

# function call with one argument
add_numbers_defaults(a=2)

# function call with no arguments
add_numbers_defaults()


# Python Keyword Argument
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name='Cartman', first_name='Eric')


# Python Function With Arbitrary Arguments
# program to find sum of multiple numbers

def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)


# Python Variable Scope
# Python Local Variables
def greet_local():

    # local variable
    message = 'Hello'

    print('Local', message)

greet_local()

# try to access message variable
# outside greet() function
# print(message)


# Python Global Variables
# declare global variable
message = 'Hello'

def greet_global():
    # declare local variable
    print('Local', message)

greet_global()
print('Global', message)


# Python Nonlocal Variables
# outside function
def outer():
    message = 'local'

    # nested function
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

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


# Example: Changing Global Variable From Inside a Function using global
# global variable
c = 1

def add_global():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2

    print(c)

add_global()

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
# import standard math module
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi)


# Python import with Renaming
# import module by renaming it
import math as m

print(m.pi)

# Output: 3.141592653589793


# Python from...import statement
# import only pi from math module
from math import pi

print(pi)

# Output: 3.141592653589793


# Import all names
# import all names from the standard module math
from math import *

print("The value of pi is", pi)


# Python Main function
# Running Python File as a Script
print(__name__)

# Using if conditional with __name__
def main():
    print("Hello World")

if __name__ == "__main__":
    main()