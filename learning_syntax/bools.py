#
# In fact, there are not many values that evaluate to False,
# except empty values, such as (), [], {}, "", the number 0, and the value None
#
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


def disable(boolean):
    return boolean

if disable(False) :
    print("It's disabled")
else:
    print("It's enabled")