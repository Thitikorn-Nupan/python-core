"""
Use a Module
Now we can use the module we just created, by using the import statement
"""
import basic_math
import info_db
## Re-naming a Module
import info_db as database
## There are several built-in modules in Python, which you can import whenever you like.
import platform
import random
## now anything on my_logger i can call on this as app.logger.debug("test")
import my_logger as app
"""
print(basic_math.plus(10,15))
print(basic_math.plus(10.9,15.9))
print(basic_math.plus(10,15.9))
"""

# print(info_db.__info) # {'username': 'user', 'email': 'user@gmail,com', 'password': '12345', 'status': True, 'timestamp': 1515151512}
# print(database.__info)
# print(platform.system()) # Windows
# print(random.choice([1,2]))


app.logger.debug("test")