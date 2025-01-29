# Multiline Strings
comments = '''
    three single quotes 
    you can write multiple lines 
'''

# or three double quotes
comments = """
    three double quotes 
    you can write multiple lines 
"""

# new line by \
comments = "after double quotes use \ "\
            "for multiple lines"\

# Strings are arrays
firstname = "Thitikorn"
# print(firstname[0]) # T
# print("length of firstname is ", len(firstname)) # 15
# print(firstname[0:10]) # Thitikorn *** way to slice string in python ** index 10 (not included)
# print(firstname[10:]) # get index 10 then ends

"""
# loop get each index
for char in firstname:
    print(char)
"""


# ******** Work string with condition
"""
#### search Nupan is in firstname ?
if "Nupan" in firstname:
    print("There is Nupan in firstname")
else:
    print("There is no Nupan in firstname")
#### search Beer is not in firstname ?
if "Beer" not in firstname:
    print("There is no Beer in firstname")
else:
    print("There is Beer in firstname")
"""

# ***** Good jobs ! F-Strings To specify a string as an f-string, simply put an f in front of the string literal,
# ***** And add curly brackets {} as placeholders for variables and other operations.
age = 18
# ***** it works like $ in type-script
# ***** F or f still work good
# print(F"{firstname} is {age} years old")
print(f"1 / 1 = {int(1 / 1)}")
print(f"firstname =  {firstname}")