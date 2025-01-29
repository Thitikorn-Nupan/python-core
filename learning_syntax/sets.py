# Sets are used to store multiple items in a single variable. *** Same tuple
# A set is a collection which is unordered, unchangeable*, and unindexed.
fruits = {"apple", "banana", "cherry"}

# ***** Duplicate values will be ignored. Sets cannot have two items with the same value.
numbersAsString = {"1", "2", "1","3"}
# print(numbersAsString) # {'3', '1', '2'}

# True and 1 is considered the same value
numbersAsObject = {"1", 2, True,False}
# print(numbersAsObject)

# Create set with ** constructs
names = set(("beer", "jey", "alun"))
# Add value to set using .add(...)
names.add("max")
names.add("tee")
# print(names)

otherNames = {"key","bee","dany"}
# Add set to set using .update(...)

names.update(otherNames)
# print(names) # {'max', 'beer', 'alun', 'jey', 'bee', 'key', 'dany'}

# Remove some value
# ** Note: If the item to remove does not exist, remove(...) will raise an error.
names.remove("key")
# Note: If the item to remove does not exist, discard(...) will NOT raise an error.
names.discard("key")

# Clear set
names.clear()


# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# allSets = set1.union(set2, set3, set4)
# Or
allSets = set1 | set2 | set3 | set4
# print(allSets)