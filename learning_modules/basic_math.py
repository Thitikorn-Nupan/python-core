"""
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
"""
# To create a module just save the code you want in a file with the file extension
# overloding
def plus(a:int,b:int):
    return a+b
def plus(a:float,b:float):
    return a+b
def plus(a:float,b:int):
    return a+b
def plus(a:int,b:float):
    return a+b


