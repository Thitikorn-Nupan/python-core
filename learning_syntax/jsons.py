"""
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
Python has a built-in package called json, which can be used to work with JSON data.
"""
import json
# If you have a JSON string, you can parse it by using the json.loads() method.
userAsJsonString =  '{"id":101, "name":"John", "age":30, "city":"New York"}'
userAsJson = json.loads(userAsJsonString)
print(userAsJson["name"]) # John

# Convert dict to json by using the json.dumps() method.
bookAsDict = {
    "id" : 101,
    "title" : "Core Android Studio 2019",
    "price":250,
    "unit":"Bath"
}

# example above prints a JSON string, but it is not very easy to read,
bookAsJsonDump = json.dumps(bookAsDict) #
# print(bookAsJsonDump) # {"id": 101, "title": "Core Android Studio 2019", "price": 250, "unit": "Bath"}

##  It is not very easy to read, with no indentations and line breaks.
##  just convert to json format using .loads(...) method will be cool
bookAsJson = json.loads(bookAsJsonDump)
print(bookAsJson["title"])


