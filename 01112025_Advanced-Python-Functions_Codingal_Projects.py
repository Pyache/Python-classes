"""List Comprehension enormously reduces the time
to process information in comparison to operators.
Use the List comprehension to do the following -

1. Take a number from the user, create a list with
all the odd numbers under the input value and
another list of odd numbers.

2. Create a list of fruits. Then, convert the first
letter of every element to capital and create a new
list of updated values.
"""


num = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, num) if i % 2 != 0]
even_numbers = [i for i in range(1, num) if i % 2 == 0]

print("List of odd numbers under", num, ":", odd_numbers)
print("List of even numbers under", num, ":", even_numbers)
fruits = ["apple", "banana", "cherry", "guava"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original list of fruits:", fruits)
print("List with capitalized fruits:", capitalized_fruits)