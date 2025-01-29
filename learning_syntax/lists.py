#
# Lists are used to store multiple items in a single variable. ** can have multiple types
# List items are indexed, the first item has index [0], the second item has index [1] etc.
#
from typing import final
fruits = ["apple", "banana", "cherry"]
result = [True,False]
objects = [1,"2",True]
# It is also possible to use the list() ** constructor when creating a new list.
ages = list((25,19,31,29))


"""
Note.
There are four collection data types in the Python programming language:
* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""



# Element*** variables it will be same type
element1To3 = fruits[1:3]  # ['banana', 'cherry']
element1To2 = fruits[1:2]  # ['banana']
element0To2 = fruits[:2]   # but not including 2
element2ToEnd = fruits[2:] # but not including 2


fruits[0] = "orange" # change list element 0
fruits[0:2]= ["orange","banana"] # change list element 0:2
# print(fruits) # ['orange', 'banana', 'cherry']

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
fruits.insert(0,"apple") # ['apple', 'orange', 'banana', 'cherry']
fruits.insert(1,"grapes") # ['apple','grapes','orange', 'banana', 'cherry']

# To append elements from another list to the current list, use the extend()
fruitsSub = ["apple", "banana"]
fruits.extend(fruitsSub) # ['apple', 'grapes', 'orange', 'banana', 'cherry', 'apple', 'banana']

### Remove Specified Item(s)
# fruits.remove("apple") # will remove 1 **  first occurrence

### Remove Specified Index
# If you do not specify the index, the pop() method removes the last item.
# fruits.pop(0)  # will remove 1


# The del keyword also removes the specified index
del fruitsSub[0] # delete element 0
# del fruitsSub # delete list
# print(fruitsSub) # NameError: name 'fruitsSub' is not defined. Did you mean: 'fruits'?


# Clear the List
fruitsSub.clear() # The list still remains, but it has no content.


# Looping
# By using a for loop
"""
for fruit in fruits:
    print(fruit)
"""

# Using a While Loop
"""
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1
"""

numbers=[1,2,3,4,5,6,7,8,9,10]
# List Comprehension ****
# *** newList = [expression for item in iterable if condition == True]
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
oddNumbers = [x for x in numbers if x%2 != 0]
evenNumbers = [x for x in numbers if x%2 == 0]
numbersLessThen3 = [x for x in numbers if x < 3]
# You can use the range() function to create an iterable
numbersHas5Elements = [x for x in range(5)] # x is 0 to 4
number = [x for x in numbers if x == 10]
# print(oddNumbers)
# print(evenNumbers)
# print(numbersLessThen3)
# print(number)
