#Python Booleans and Boolean Expressions
#python boolean 

#Comparison Operators Example: < and <=
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = (x < y)
print(f"x < y ---> {result}")

result = (x <= y)
print(f"x <= y ---> {result}")

result = (x < 10)
print(f"x < 10 ---> {result}")

result = (x <= 10)
print(f"x <= 10 ---> {result}")
print()


#Example: > and >=
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = (x > y)
print(f"x > y ---> {result}")

result = (x >= y)
print(f"x >= y ---> {result}")

result = (x > 10)
print(f"x > 10 ---> {result}")

result = (x >= 10)
print(f"x >= 10 ---> {result}")
print()

#Example: == and !=
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = (x == y)
print(f"x == y ---> {result}")

result = (x != y)
print(f"x != y ---> {result}")

result = (x == 10)
print(f"x == 10 ---> {result}")

result = (x != 10)
print(f"x != 10 ---> {result}")

result = (not x == 10 or not y == 10)
print(f"not x == 10 or not y == 10 ---> {result}")
print()

name1 = "HanTaesan"    

print(name1 == "HanTaesan")   # True
print(name1 == "HanTaesan")   # False
print(name1 != "HanTaesan")   # False
print(name1 != "HanTaesan")   # True
print()


#Logical Operators
#The and Operator
age = int(input("Enter your age: "))
citizen = input("Korean citizen (yes/no)?: ")

# True only if (age >= 17) 
# and
# (citizen == "yes") is True
result = (age >= 17) and (citizen == "yes")
print(result)
print()


#The or Operator
age = int(input("Enter your age: "))
citizen = input("Korean citizen (yes/no)?: ")

# True if either (age >= 17)
# or
# (citizen == "yes") is True
result = (age >= 17) or (citizen == "yes")
print(result)
print()


#The not Operator
passcode = "1234"
entered_code = input("Enter passcode: ")

result = (passcode == entered_code)
print(f"Is passcode equal to entered code? {result}")

result = not (passcode == entered_code)
print(f"Is passcode not equal to entered code? {result}")
print()


#The bollean() Function
# 0 is False
print(bool(0))

# Non-zero value is True
print(bool(13))

# Non-empty string is True
print(bool("Python"))
print(bool("False"))  # True

# Empty string is False
print(bool(""))
print(bool(None))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(()))  # False
print(bool(set()))  # False
print(bool(range(0)))  # False
print(bool(range(1)))  # True
print(bool(range(10)))  # True
print(bool(range(-10)))  # True
print(bool(range(-1)))  # True
print()
print()



#Python if...else Statement
#Example: Python if Statement
age = int(input("Enter your age: "))

# Check if age is 17 or more
if age >= 17:
    print("Grant access to the website.")

print("Program complete.")
print()


#Indentation in Python
age = int(input("Enter your age: "))

if age >= 17:
    print("Grant access to the website.")

print("Program complete.")
print()


#Python if…else Statement
age = int(input("Enter your age: "))

if age >= 17:
    print("Grant access.")
else:
    print("Deny access.")
    print("You must be 17 or older to access this website.")
    print("Program complete.")
    print()    
    
    
#Authenticate User Logic Using if...else
# Username and password stored in database
username_db = "Cat"
password_db = "bohit3"

# Username and password entered by the user
username = input("Enter username: ")
password = input("Enter password: ") 

# Check if username & password in database matches user's input
if (username == username_db) and (password == password_db):
    print("Allow.")
else:
    print("Access denied.")
    print()
    
    
#Python if…elif…else Statement
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age >= 17:
    print("Grant access.")
else:
    print("Deny access.")
    
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age < 17:
    print("Deny access.")
elif age >= 17:
    print("Deny access.")
    print()
    
    
#Nested if Statements
age = int(input("Enter your age: "))

# Condition to check if age is less than 17
if age < 17:

    # If age is less than 17, condition to check if it's negative
    if age < 0:
        print("Invalid age.")
    else:
        print("Deny access.")
else:
    print("Grant access.")
    print()
    
    
#Short Hand if...else
age = 22
status = "Adult" if age >= 17 else "Minor"
print(status)
print()

age = 22

if age >= 17:
    status = "Adult"
else:
    status = "Minor"
    print(status)
    print()
    

#Largest of Three Numbers
# Taking input from the user
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3

print("The largest number is:", largest)
print ()
print()


#Python for loop 
#Iterating trought a List

# A list of three AI models
models = ["Fable", "ChatGPT", "Gemini"]

# Access items of the list one by one
for model in models:
    print(model)
    print("---")
    print("End of list.")
    print()
 
#Identation in loop
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"Processing: {num}")
    print(f"Done with: {num}")

# This statement is outside the loop
print('All done')
print ()    


#For Loop with python range() 
# Iterate from i = 1 to i = 10
for i in range(1, 11):
    print(f"Displaying product {i}")
print()


#Iterating through a String
language = 'Python'

for x in language:
    print(x)
print()

#Break and continue Statements
#The Break Statement
for num in range(1, 11):
    if num == 3:
        break
    print(num)
print()


#The Continue Statement
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
print()


#For Loop with else
stock = ['Moca', 'Matcha', 'Cheese']

order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")
    print()
    
    

#Using for Loop Without Using Items
# Iterate from i = 0 to 3
for _ in range(0, 5):
    print("ola!")
print()


#Sum of Natural Numbers
# Initial value of sum is 0
total = 0

# Iterate from i = 1 to 10
for i in range(1, 11):
    total += i   # Add i to total in each step

print(f"Total = {total}")
print()


#Nested for Loops
attributes = ['Icy', 'Sweet']
drink = ['Water', 'Coffee', 'Tea']

for attribute in attributes:
    for drink in drink:
        print(attribute, drink)

    print("-----")
    print()
    

#Python while loop
#Example: Infinite while Loop
number = float(input("Enter a number: "))

while number >= 0.0:
    print(number)
    number = float(input("Enter another number: "))

print("End of loop.")
print()

#Example: Finite while Loop
number = float(input("Enter a number: "))

while number >= 0.0:
    print(number)
    
    # Take number input again
    number = float(input("Enter another number: "))
print("End of loop.")
print()

    
#Indentation
task = input("Task: ")

while task != "q":
    print("Task done!")
    task = input("Task: ")

# This statement is outside the loop
print("All tasks completed")
print()


#Print Numbers from 1 to n
n = 10
i = 1

while i <= n:
    print(i)
    i += 1 
    print()
    
n = 10

# Iterate from i = 1 to n
for i in range(1, n+1):
    print(i)
    print()
    
    
#Sum Numbers Until User Enters Zero
total = 0
n = float(input("Enter a number (0 to stop): "))

while n != 0.0:
    total += n
    n = float(input("Enter a number (0 to stop): "))

print(f"Sum: {total}")
print()


#Break and Continue Statements
#The break Statement
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    print(number)
    print()
    
    
#The continue Statement
i = 0

while i <= 10:
    i += 1
    
    # Skip odd numbers
    if i % 2 != 0:
        continue

    print(i)
    print()
    
    
#While Loop with Else Clause
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == "1324":
        print("Access granted.")
        break

    attempts -= 1
    print(f"Wrong PIN. {attempts} tries left.")
else:
    print("Account locked. Too many failed attempts.")
    print()
    
    
    
#Python break and continue
#Python break Statement, Example: break in for Loop
number = int(input("Enter a number: "))
for i in range(1, 6):

    # Terminate the loop if i equals number
    if i == number:
        break
    print(i)
    print()
    
    
#break in while loop 
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    print(f"You entered {number}")
    print()
    
    
#Python continue Statement, Example: continue in for Loop
for i in range(1, 11):

    # Condition to check if a number is even
    if i % 2 == 0:
        continue
    print(i)
    print()
    
    
#Sum of Only Positive Numbers
total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    # Skip negative numbers
    if number < 0:
        continue

    # End the loop if the user enters 0
    if number == 0:
        break

    total += number

print(f"Sum of positive numbers: {total}")
print()


#Loop with else Clause
stock = ['Latte', 'Matcha', 'Cheese']

order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")
    print() 
    
    
#Python pass Statement
#pass Statement
for i in range(1, 5):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(i)
        print()
        
is_valid = True

if is_valid:
    pass
else:
    print("Login invalid. Redirect to form.")
    print()