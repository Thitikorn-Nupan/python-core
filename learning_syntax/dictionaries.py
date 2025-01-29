"""
Dictionary
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""

infoDB = {
    "username": "user",
    "email": "user@gmail,com",
    "password": "12345",
    "status": True,
    "timestamp": 1515151512
}

# print(infoDB) # {'username': 'user', 'email': 'user@gmail,com', 'password': '12345', 'status': True, 'timestamp': 1515151512}
# print(infoDB["username"]) # use .get(<key>) or [<key>] for retrieve a value

## Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
infoDB["username"] = "test"
## The update() method will update the dictionary with the items from the given argument.
infoDB.update({"username": "admin"})
infoDB.update({"email": "admin@gmail,com"})
# print(infoDB) # {'username': 'test', ...
# print(type(infoDB)) # <class 'dict'>

## It is also possible to use the dict() constructor to make a dictionary.
secretInfoDriver = dict(database="mysql", driver="com.mysql.cj.jdbc.Driver", url="jdbc:mysql://127.0.0.1:8080")
database = secretInfoDriver["database"]  # or database = secretInfoDriver.get("database")

# print(secretInfoDriver) # {'database': 'mysql', 'driver': 'com.mysql.cj.jdbc.Driver', 'url': 'jdbc:mysql://127.0.0.1:8080'}

## The keys() method will return a list of all the keys in the dictionary.
keys = secretInfoDriver.keys()  # keys =  dict_keys(['database', 'driver', 'url'])
values = secretInfoDriver.values()  # dict_values(['mysql', 'com.mysql.cj.jdbc.Driver', 'jdbc:mysql://127.0.0.1:8080'])

## Note! if secretInfoDriver changes , keys and values change too
# print(values)
secretInfoDriver["database"] = "mariadb"
# print(values)


## The items() method will return each item in a dictionary, as tuples in a list.
infoDriverAsTuple = secretInfoDriver.items()  # dict_items([('database', 'mariadb'), ('driver', 'com.mysql.cj.jdbc.Driver'), ('url', 'jdbc:mysql://127.0.0.1:8080')])
# print(infoDriverAsTuple)


## Work with condition
"""
if "driver" in secretInfoDriver:
    print("driver fucking exists")
"""

## Nested Dictionaries A dictionary can contain dictionaries, this is called nested dictionaries.
users = {
    "user1": {
        "fullname": "alex ryder",
        "age": 35
    },
    "user2": {
        "fullname": "kevin own",
        "age": 32
    },
    "user3": {
        "fullname": "jon parker",
        "age": 36
    }
}

# print(users["user1"]["fullname"]) # alex ryder



# user1 = {
#     "fullname": "alex ryder",
#     "age": 35
# },
# user2 = {
#     "fullname": "kevin own",
#     "age": 32
# },
# user3 = {
#     "fullname": "jon parker",
#     "age": 36
# }
#
# ## Same thing with on top
# users = {
#     "users1" : user1,
#     "users2" : user2,
#     "users3" : user3
# }

## Loop Through Nested Dictionaries
for x , obj in users.items():
    """
    print(x)
    users1
    users2
    users3

    print(obj)
    ({'fullname': 'alex ryder', 'age': 35},)
    ({'fullname': 'kevin own', 'age': 32},)
    {'fullname': 'jon parker', 'age': 36}
    """
    ## ended for x
    for y in obj:
        print(f" {y} : {obj[y]}")
        # ended for y