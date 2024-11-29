student_inform1 = {
    "name": 'Aman',
    "age": '35',
    "role": 'SDET',
    "experience": 5,
    "address": {
        "home_address": "ND",
        "Office_address": "KA"
    }
}

student_inform2 = {
    "name": 'Pramod',
    "age": '30',
    "role": 'testing',
    "experience": 3,
    "address": {
        "home_address": "GOA",
        "Office_address": "TN"
    }
}

student_list    = [student_inform1,student_inform2]
print(student_list)     #Display all the records inside list
print(student_list[0])  #Only display first record
print(student_list[0]["name"])  #Display the name from first elemnt
print(student_list[1]['name'])  #Display the name from 2nd element
print(student_list[0]["address"]["home_address"])
print(student_list[1]["address"]["home_address"])
