"""
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
"""
## Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
fruitsList = ["apple", "banana", "cherry"]
fruitsIterator = iter(fruitsList)
# print(fruitsIterator) # <list_iterator object at 0x000001D9A0492CE0>
print(next(fruitsIterator)) # "apple"
print(next(fruitsIterator)) # "banana"

## Even strings are iterable objects, and can return an iterator
fruitString = "apple"
fruitsIterator = iter(fruitString)
print(next(fruitsIterator)) # a
print(next(fruitsIterator)) # p




"""
The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""
class InAndDecrementsNumbers :
    def __init__(self,number : int):
        self.numberStartByUser = number

    def __iter__(self):
        self.numberStartByClass = 1
        return self

    def __next__(self):
        self.numberStartByClass -= 1
        self.numberStartByUser += 1
        if self.numberStartByUser == 5 :
            return self.numberStartByUser
        else:
            # raise works like throw
            raise StopIteration
    def __str__(self):
        return f"user : {self.numberStartByUser} , class : {self.numberStartByClass}"


inAndDecrementsNumbers = InAndDecrementsNumbers(5)
# If your class has __iter__ method you have to convert to iter object
inAndDecrementsNumbersIter = iter(inAndDecrementsNumbers) #
print(inAndDecrementsNumbers)
# after call __next__() x3 method
inAndDecrementsNumbersIter.__next__()
inAndDecrementsNumbersIter.__next__()
inAndDecrementsNumbersIter.__next__()
print(inAndDecrementsNumbers)
