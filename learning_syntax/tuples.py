# Tuples are used to store multiple items in a single variable. ** can has multiple types in tuple
# *** Tuple items are ordered, *** unchangeable, and allow duplicate values.
fruits = ("apple", "banana", "cherry")
objects = (1,"2",True)
# print(fruits[0]) # apple
# print(len(fruits)) # 3

# It is also possible to use the tuple() ** constructor to make a tuple.
numbers = tuple((1,2,3,4,5))

# print(numbers)
element1To3 = numbers[1:3] # not include 3 (2, 3)
element1To2 = numbers[1:2] # (2,)
element0To2 = numbers[:2] # but not including 2 (1, 2)
element2ToEnd = numbers[2:] # (3, 4, 5)

print(element1To3)
print(element1To2)
print(element0To2)
print(element2ToEnd)

"""
### Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
### if you want do this way Convert the tuple into a list to be able to change it
### Example 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
"""

## Unpacking a Tuple
(one,two,three,four,five) = numbers # it will map follow elements

# Join Two Tuples
numbersSub = tuple((6,7,8,9))
mergeNumbers = numbers + numbersSub
print(mergeNumbers) # (1, 2, 3, 4, 5, 6, 7, 8, 9)