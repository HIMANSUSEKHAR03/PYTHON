## JSON stands for JavaScript Object Notation.

#It is a lightweight format used to store and exchange data. It is widely used in web apps, APIs, configuration files, and Python projects.
#Basic structure:

#JSON uses key-value pairs
#Keys are strings in double quotes
#Values can be:
#string
#number
#object
#array
#boolean
#null


#Example:
{
  "name": "Alice",
  "age": 25,
  "isStudent": True,
  "skills": ["Python", "JavaScript"],
  "address": {
    "city": "New York",
    "country": "USA"
  }
}

#Why JSON is useful:
# Easy to read
# Easy to write
# Language-independent
# Commonly used with APIs

#In Python:
import json

data = '{"name": "Alice", "age": 25}'
obj = json.loads(data)   # string to Python dict
print(obj["name"])       # Alice

new_data = json.dumps(obj)  # dict to JSON string
print(new_data)

#Common JSON terms:
# JSON object = {}  
# JSON array = []  
#JSON string = ""  
# JSON number = 123  
# JSON boolean = true / false  
# JSON null = null  
#Here are common examples of converting JSON into Python objects:


import json

# 1) JSON string to Python dict
json_string = '{"name": "Alice", "age": 25, "isStudent": true, "skills": ["Python", "JavaScript"]}'
data = json.loads(json_string)

print(data)
print(type(data))   # <class 'dict'>
print(data["name"]) # Alice
print(data["age"])  # 25
print(data["skills"][0])  # Python

#Output:
{'name': 'Alice', 'age': 25, 'isStudent': True, 'skills': ['Python', 'JavaScript']}

#Important:
# JSON boolean: true/false  -> Python: True/False
# JSON null -> Python: None
# JSON array -> Python list
# JSON object -> Python dict

#Example with null:
#python
json_string = '{"name": "Bob", "active": false, "city": null}'
data = json.loads(json_string)

print(data["active"])  # False
print(data["city"])    # None


