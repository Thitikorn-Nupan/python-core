# These are Global Variables
x = 4  # x is of type int
x = "Hello World"  # x is now of type string

# If you want to specify the data type of a variable
y = str("Hello World")  # x will be 'Hello World'
y = int(1)  # y will be 1
y = float(1)  # y will be 1.0

# print(type(y)) # check data type using type(y) => <class 'float'>

x = 1000
y = 500
# ****** Multi Words Variable Names
# ****** Camel case
xDivideY = x / y
xPlusY = x + y
xMinusY = x - y


# ****** Snake case
x_multiply_y = x * y
# print(xDivideY, xPlusY, xMinusY, x_multiply_y) # 2.0 1500 500 500000

# ****** Many Values to Multiple Variables
xDivideY, xPlusY, xMinusY = x / y , x + y , x - y

# ****** One Value to Multiple Variables
resultAOfXDivideY = resultBOfXDivideY = resultCOfXDivideY = xDivideY
# print(xDivideY, xPlusY, xMinusY, x_multiply_y)  # 2.0 1500 500 500000
# print(resultAOfXDivideY+resultBOfXDivideY+resultCOfXDivideY)

# ****** Unpack a Collection ** You can mix type on collection
fruits = ["apple", "banana", "cherry"] # list
print(fruits) # ['apple', 'banana', 'cherry']
print(fruits[0]) # apple

data = [1, 2, "3"]
print(data) # [1, 2, '3']


def myPrint():
    # Local variable
    data = { # dict types
        "username" :"austin",
        "age":29,
        "status" : True
    }
    print(data)
    print(data.get("status"))

myPrint()