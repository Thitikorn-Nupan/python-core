"""
***Exception Handling****
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""
# *** To throw (or raise) an exception, use the raise keyword.
try:
  x = 10
  y = x/0
except ZeroDivisionError:
  print("Stupid division")
except:
    print("Something else went wrong")
else:
    print("No error")
finally:
    print("The 'try except else' is finished")


x = "-1"
"""
if x < 0:
  raise Exception("Sorry, no numbers below zero")
"""
if not type(x) is int:
  raise TypeError("Only integers are allowed")

