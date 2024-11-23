greeting = 'Today is bright sunny day'
print(len(greeting))
words = greeting.split()
print(words)
_greet = 'hello world'
print(_greet[8:-9:-1])
# In Python, the syntax (8:-9:-1) is used for slicing a sequence
# (like a string, list, or tuple) with a negative step. Let's break it down:
# Start: 8. This is the index where the slice starts.
# Stop: -9. This is the index where the slice ends (not including the element at this index).
# Step: -1. This indicates that the slice should move backward through the sequence.
print(len(_greet))
print(_greet[0:5:1])

name = 'john'
age = 35
pay = 100000
print(f"Hello {name} you are {age} old and and your salary is ${pay}")
