import requests
import json
import csv

# python object(dictionary) to be dumped
dict1 = {
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}

print(dict1)
# the json file where the output must be stored
# dump() : which converts the Python objects into appropriate json objects.
out_put_file = open(file=" myfile.json", mode='w')
json.dump(dict1,out_put_file,indent=6)



out_put_file.close()