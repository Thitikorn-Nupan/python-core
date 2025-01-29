import random

"""
x = "Hello World"	# str
x = 20	            # int
x = 20.5            # float
x = 1j	            # complex
x = ["apple", "banana", "cherry"]	            # list
x = ("apple", "banana", "cherry")	            # tuple
x = range(6)                                    # range
x = {"name" : "John", "age" : 36}	            # dict work like json
x = {"apple", "banana", "cherry"}	            # set
x = frozenset({"apple", "banana", "cherry"})	# frozenset
x = True	                # bool
x = b"Hello"	            # bytes
x = bytearray(5)            # bytearray
x = memoryview(bytes(5))	# Memory view
x = None	                # NoneType
"""

numbersAsList = [1, 2, 3]
## print(numbersAsList[0]+numbersAsList[1]+numbersAsList[2])
numbersAsTuple = (1, 2, 3)
## print(numbersAsTuple[0])
numbersAsSet = {1, 2, 3} # set can't get element you should covert it first
## numbersAsSet.add(4)
## print(list(numbersAsList)[2])
oneToTen = random.randrange(1,11) ## random between 1 and 10
# print(oneToTen)

