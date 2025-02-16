# https://httpbin.org/
# What is JSON?
"""
 * JSON stands for **Java Script Object Notation**
 * A standardised format commonly used for data transfer.
 * Readable both of Humans and Machine.
 * Used in Databases and API's.
 * XML is one more format used for data transfer.
 """
import requests
import json
import csv

# Serialising data into JSON file.
# Let's consider a python dictionary
info ={
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {"firstname": "Alice",
         "age": 6
         },
        {
            "firstname": "Bob",
            "age": 9
        }
    ]
}
print(info)

# Serialising data into JSON file.
with open("data.json",mode='w') as f:
    json.dump(info,f,indent=4)

