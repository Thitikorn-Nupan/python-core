"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""

## In Python a function is defined using the def keyword:
def plusNumbers(x,y) :
    print(f"x + y = {x+y}")
    # end func

def minusNumbers(x,y) :
    print(f"x - y = {x-y}")
    # end func

## Default Parameter Value
def divideNumber(x,y=1):
    print(f"x / y = {x / y}")

# plusNumbers(5,500)
# minusNumbers(5,500)
# divideNumber(5,5)
### *** Keyword Arguments
# plusNumbers(y=-95,x=50)


## Arbitrary Arguments, *args
# If you do not know how many ** arguments ** that will be passed into your function, add a *
"""
def findSigma(*numbers):
    sigma = 0
    detail = ""
    i = 0
    for x in numbers:
        i = i+1
        sigma += x
        detail += f"{x}+"
        if  i > len(numbers) :
            pass
        elif i == len(numbers):
            detail += "0="
    print(f"{detail} {sigma}")
findSigma(1,2,3,4,5,6,7,8,9,10)

"""
## Arbitrary Keyword Arguments, **kwargs
# If you do not know how many ** keyword arguments ** that will be passed into your function, add two asterisk: **

def displayDetail (**user):
    print(f"fullname is {user.get('fullname')} and age is {user.get('age')}")

# displayDetail(fullname="jack jack",age=35)

def displayList(numbers) :
    result = ""
    for x in  numbers :
        result += f"{x} "
    print(result)

# displayList([1,2,3])


#### Return Values

def findSigma(*numbers):
    sigma = 0
    detail = ""
    i = 0
    for x in numbers:
        i = i+1
        sigma += x
        detail += f"{x}+"
        if  i > len(numbers) :
            pass
        elif i == len(numbers):
            detail += "0="
    return f"{detail} {sigma}"

# print(findSigma(1,2,3,4,5))

### Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments,
# add , / after the arguments:
def multiplyNumbers(x,y,/): # can not pass argument like (y=5,x=5)
    return f"{x} * {y} = {x*y}"

# Without /
def multiplyNumbersWithoutSlash(x,y): # can pass argument like (y=5,x=5)
    return f"{x} * {y} = {x*y}"

# print(multiplyNumbers(5,5))
# print(multiplyNumbersWithoutSlash(y=5,x=5))

## To specify that a function can have only keyword arguments,
#  add *, before the arguments
def modNumbers(*,x,y) :
    return f"{x} % {y} = {x%y}"

xModY = modNumbers(x=100,y=250)
print(xModY)