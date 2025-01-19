portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(portfolio)
print("===========================================================================")
def get_share_amount(item):
    return item['shares']

#By default, it is sorted in ascending order
print(sorted(portfolio,key=get_share_amount))
print("===========================================================================")
#sort based on name
name_sort= sorted(portfolio,key=lambda item:item.get('name'))
print(name_sort)
print("===========================================================================")

#2nd Problem
students = [
    {"name": "john", "grade": "J", "age": 26},
    {"name": "kite", "grade": "B", "age": 28},
    {"name": "dave", "grade": "E", "age": 22}
]

print(sorted(students,key=lambda item:item.get("age")))
print("===========================================================================")
print(sorted(students,key=lambda item:item.get("grade")))
print(sorted(students,key=lambda item:item.get("name")))

