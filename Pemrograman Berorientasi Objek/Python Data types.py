# Python Numbers, Type Conversion and Mathematics
# Python Numeric Data Type
num1 = 4
print(num1, 'is of type', type(num1))

num2 = 4.43
print(num2, 'is of type', type(num2))

num3 = 6 + 4j
print(num3, 'is of type', type(num3))

print()

# Number Systems
print(0b1101011)  # prints 107

print(0xFB + 0b10)  # prints 253

print(0o15)  # prints 13

print()

# Type Conversion in Python
print(1 + 2.0)  # prints 3.0

num1 = int(2.3)
print(num1)  # prints 2

num2 = int(-2.8)
print(num2)  # prints -2

num3 = float(5)
print(num3)  # prints 5.0

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)

print()

# Python Random Module
import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())

print()

# Python Mathematics
import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))

print()

# Python Lists
# Creating a List

cart = ["glass", "Trash", "Phone"]
print(cart)

# A list of mixed data types
my_list = [1, "Python", 3.14]
print(my_list)

# Empty list
my_list = []
print(my_list)

vowels = "aeiou"

# Convert a string to a list
vowels_list = list(vowels)
print(vowels_list)

languages = ["Python", "Swift", "C++"]

# Access the first item
print(f"languages[0] = {languages[0]}")

# Access the third item
print(f"languages[2] = {languages[2]}")

print()

# Negative Indexing
languages = ["Python", "Swift", "C++"]

# Access the last item
print('languages[-1] =', languages[-1])

# Access the third last item
print('languages[-3] =', languages[-3])

print()

# Adding and Updating Items

cart = ["glass", "Trash", "Phone"]

# Update second item to "Shoes"
cart[1] = "Shoes"

print(cart)  # ['glass', 'Shoes', 'Phone']

cart = ["glass", "Trash", "Phone"]

# Add "Book" to the list
cart.append("Book")

print(cart)  # ['glass', 'Trash', 'Phone', 'Book']

cart = ["glass", "Trash", "Phone"]
fav_items = ["Headphones", "Handbag"]

# Add all the items from fav_items to cart
cart.extend(fav_items)

print(cart)  # ['glass', 'Trash', 'Phone', 'Headphones', 'Handbag']

cart = ["glass", "Trash", "Phone"]

# Add "Book" at index 2 (3rd position)
cart.insert(2, "Book")

print(cart)  # ['glass', 'Trash', 'Book', 'Phone']

print()

# Remove Items From a List

cart = ["glass", "Trash", "Phone", "Book"]

# Remove "Phone" from the list
cart.remove("Phone")  # ['glass', 'Trash', 'Book']

# Remove the last item
last_item = cart.pop()
print(cart)  # ['glass', 'Trash']
print(last_item)  # Book

# Clear the list
cart.clear()
print(cart)  # []

cart = ['glass', 'Trash', 'Phone', 'Book']

# Delete the third item (index 2)
del cart[2]
print(cart)  # ['glass', 'Trash', 'Book']

# Delete the list itself
del cart

print()

# Copying a List
favorite_items = ["glass", "Trash", "Phone"]

cart = favorite_items

# Add an item to favorite_items list
favorite_items.append("Book")

print(f"favorite_items = {favorite_items}")
print(f"cart = {cart}")

favorite_items = ["glass", "Trash", "Phone"]

# Copying a list
cart = favorite_items.copy()

# Add an item to favorite_items list
favorite_items.append("Book")

print(f"favorite_items = {favorite_items}")
print(f"cart = {cart}")

print()

# Python List Methods
# The len() Function
favorite_items = ["glass", "Trash", "Phone"]

size = len(favorite_items)
print(size)  # 3

print()

# List Membership Test
cart = ["glass", "Trash", "Phone"]

result = "Trash" in cart
print(result)  # True

result = "Book" in cart
print(result)  # False

print()

# Iterating Through a List
cart_items = ["glass", "Trash", "Phone"]

for item in cart_items:
    print(item)

print()

# Python Tuples
# Creating a Tuple
# empty tuple
my_tuple = ()

# tuple having integers
my_tuple = (1, 2, 3)

# tuple with mixed datatypes
my_tuple = (1, "Bonjour", 3.4)

# nested tuple
my_tuple = ("bird", [8, 4, 6], (1, 2, 3))

# tuple can be created without parentheses
# also called tuple packing
my_tuple = 3, 4.6, "cat"
# tuple unpacking is also possible
a, b, c = my_tuple

my_tuple = "Bonjour"  # only parentheses is not enough
print(type(my_tuple))  # <class 'str'>

my_tuple = ("Bonjour",)  # need a comma at the end
print(type(my_tuple))  # <class 'tuple'>

my_tuple = "Bonjour",  # parentheses is optional
print(type(my_tuple))  # <class 'tuple'>

print()

# Accessing Elements in a Tuple
# Indexing
my_tuple = ['p', 'e', 'r', 'm', 'i', 't']
print(my_tuple[0])  # 'p'
print(my_tuple[5])  # 't'

# Catatan: my_tuple[6] akan menyebabkan IndexError (index out of range)
# Catatan: my_tuple[2.0] akan menyebabkan TypeError (indices must be integers, not float)

n_tuple = ("bird", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3])  # nested index: 'd'
print(n_tuple[1][1])  # nested index: 4
print(n_tuple[2][0])  # nested index: 1

print()

# Negative Indexing
my_tuple = ['p', 'e', 'r', 'm', 'i', 't']
print(my_tuple[-1])  # 't'
print(my_tuple[-6])  # 'p'

print()

# Slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[1:4])  # elements 2nd to 4th: ('r', 'o', 'g')
print(my_tuple[:-7])  # elements beginning to 2nd: ('p', 'r')
print(my_tuple[7:])  # elements 8th to end: ('i', 'z')
print(my_tuple[:])  # elements beginning to end

# *---*---*---*---*---*---*---*---*---*
#  | p | r | o | g | r | a | m | i | z |
#  *---*---*---*---*---*---*---*---*---*
#  0   1   2   3   4   5   6   7   8   9
# -9  -8  -7  -6  -5  -4  -3  -2  -1

print()

# Changing or Deleting a Tuple
my_tuple = (4, 2, 3, [6, 5])
# Catatan: my_tuple[1] = 9 -> TypeError (we cannot change an element)
# Catatan: my_tuple[3] = 9 -> TypeError (we cannot change an element)

my_tuple[3][0] = 9  # but item of mutable element can be changed
print(my_tuple)  # (4, 2, 3, [9, 5])

my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')  # tuples can be reassigned
print(my_tuple)

print((1, 2, 3) + (4, 5, 6))  # (1, 2, 3, 4, 5, 6)
print(("Repeat",) * 3)  # ('Repeat', 'Repeat', 'Repeat')

my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# Catatan: del my_tuple[3] -> TypeError (can't delete items)

del my_tuple  # can delete entire tuple

print()

# Python Tuple Methods

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.count('p'))  # 2
print(my_tuple.index('l'))  # 3

print()

# Other Tuple Operations
# Tuple Membership Test
my_tuple = ('a', 'p', 'p', 'l', 'e')
print('a' in my_tuple)  # True
print('b' in my_tuple)  # False
print('g' not in my_tuple)  # True

print()

# Iterating
for name in ('Taesan', 'Gue'):
    print("Hello", name)

print()

# Python Strings
# Python Multiline Strings
# Multiline string
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)

print()

# Access String Characters
model = 'ChatGPT'

# Access the first character
print(model[0])  # Output: C

# Access the fifth character
print(model[4])  # Output: G

model = 'ChatGPT'

# Access the last character
print(model[-1])  # Output: T

# Access the fourth last character
print(model[-4])  # Output: t

model = 'ChatGPT'
# Catatan: print(model[8]) -> IndexError

# Access characters from index 0 up to (but not including) 4
print(model[0:4])  # Output: Chat

print()

# Strings are Immutable
model = 'ChatGPT'

# Catatan: model[0] = 'W' -> TypeError (Strings are immutable)

model = 'BND'
version = '5'

model = model + " " + version
print(model)  # BND 5

print()

# Python String Methods
text = "ChatGPT is great."

# Replace "ChatGPT" with "Claude"
new_text = text.replace("ChatGPT", "Claude")

print(new_text)  # Output: Claude is great.

print()

# String Membership Test
print('Chat' in 'ChatGPT')  # True
print('Claude' not in 'ChatGPT')  # True

print()

# Iterate Through a String
model = 'BND'

for c in model:
    print(c)

print()

# Python String Length
model = 'BND'

# Count the number of characters
print(len(model))  # Output: 4

print()

# Escape Sequences
# Catatan: example = "She said, "Your so Cool"" -> SyntaxError

# escape double quotes
example = "She said, \"Your so Cool\""

# escape single quotes
example = 'She said, "Your so Cool"'

print(example)

# Output: She said, "Your so Cool"

print()

# String Formatting (f-Strings)
company = 'Google'
field = 'AI'

message = f'{company} is an {field} company.'
print(message)

print()

# Python Sets
# Create a Set in Python
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Bonjour', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

print()

# Create an Empty Set in Python
# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary:', type(empty_dictionary))

print()

# Add and Update Set Items in Python
# Add Items to a Set in Python
numbers = {30, 37, 67, 78}

print('Initial Set:', numbers)

# using add() method
numbers.add(33)

print('Updated Set:', numbers)

print()

# Update Python Set
companies = {'Prada', 'Gucci'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Gucci', 'Prada'}

print()

# Iterate Over a Set in Python
fruits = {"Melon", "Orange", "Grape"}

# for loop to access each fruits
for fruit in fruits:
    print(fruit)

print()

# Find Number of Set Elements
even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)

# find number of elements
print('Total Elements:', len(even_numbers))

print()

# Python Set Operations
# Union of Two Sets
# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B))

print()

# Set Intersection
# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

print()

# Difference between Two Sets
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using -
print('Difference using -:', A - B)

# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

print()

# Set Symmetric Difference
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using ^
print('using ^:', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))

print()

# Check if two sets are equal
# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform check
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')

print()

# Python Dictionary
# Create a Dictionary
# creating a dictionary
country_capitals = {
    "Malaysia": "Kuala Lumpur",
    "Philippines": "Manila",
    "Singapore": "Singapore"
}

# printing the dictionary
print(country_capitals)

print()

# Access Dictionary Items
country_capitals = {
    "Malaysia": "Kuala Lumpur",
    "Philippines": "Manila",
    "Singapore": "Singapore"
}

# access the value of keys
print(country_capitals["Malaysia"])  # Output: Kuala Lumpur
print(country_capitals["Philippines"])  # Output: Manila

print()

# Add Items to a Dictionary
country_capitals = {
    "Malaysia": "Kuala Lumpur",
    "Philippines": "Manila",
}

# add an item with "France" as key and "Paris" as its value
country_capitals["France"] = "Paris"

print(country_capitals)

print()

# Remove Dictionary Items
country_capitals = {
    "Malaysia": "Kuala Lumpur",
    "Philippines": "Manila",
}

# delete item having "Malaysia" key
del country_capitals["Malaysia"]

print(country_capitals)

country_capitals = {
    "Malaysia": "Kuala Lumpur",
    "Philippines": "Manila",
}

# clear the dictionary
country_capitals.clear()

print(country_capitals)

country_capitals = {
    "Malaysia": "Kuala Lumpur",
    "Philippines": "Manila",
}

# clear the dictionary
country_capitals.clear()

print(country_capitals)

print()

# Change Dictionary Items
country_capitals = {
    "Malaysia": "Kuala Lumpur",
    "Philippines": "Manila",
    "France": "Paris"
}

# change the value of "Philippines" key to "Manila" (no change needed in this case)
country_capitals["Italy"] = "Rome"

print(country_capitals)

print()

# Iterate Through a Dictionary
country_capitals = {
    "South Korea": "Seoul",
    "Italy": "Rome"
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

print()

# Find Dictionary Length
country_capitals = {"South Korea": "Seoul", "Italy": "Rome"}

# get dictionary's length
print(len(country_capitals))  # Output: 2

numbers = {10: "ten", 20: "twenty", 30: "thirty"}

# get dictionary's length
print(len(numbers))  # Output: 3

countries = {}

# get dictionary's length
print(len(countries))  # Output: 0

print()

# Dictionary Membership Test
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)  # Output: True
print(".mp3" in file_types)  # Output: False
print(".mp3" not in file_types)  # Output: True