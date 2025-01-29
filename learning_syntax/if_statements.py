x = 20
y = 15
message = ""

## If...else
"""
if x == y :
    message = "x = y"
else:
    message = "x != y"
"""

## If...Elif
"""
if x == y :
    message = "x = y"
elif x > y :
    message = "x > y"
elif x < y :
    message = "x < y"
else:
    message = "x != y"
"""


## Short Hand If
if x == y : print("x = y")

## Short Hand If ... Else
print("x = y") if x == y else print("x != y")


## The and keyword is a logical operator, and is used to combine conditional statements:
if x != y and x == 20 :
    print("True and True are True")

## The or keyword is a logical operator, and is used to combine conditional statements:
if x == y or x == 20 :
    print("False or True are True")

## The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
## Work like a logic
## ~True = False
if not False :
    print("~False is True")