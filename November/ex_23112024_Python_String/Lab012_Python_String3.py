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
# f strings or formatted strings
print(f"Hello {name} you are {age} old and and your salary is ${pay}")
print("hello {name} you are {age} years of age")

# "in" is called membership operator
print("h" in _greet)
print('f' in _greet)

# range(start_index, end_index, step_size)
greeting = "hello world"
for i in greeting:
    print(i)

for i in range(0, 5):
    print(i)

for i in range(0, 20, 2):
    print(i)

# find odd and even number range is 0-50
for i in range(0, 50):
    if i % 2 == 0:
        print("even", i)
    else:
        print('odd', i)
# Print the numbers in reverse order
for num in range(10,0,-1):
    print(num)

for num in range(100,0,-10):
    print(num)

for i in range(0,5):
    print("Hello Pramod")

for i in range(0,len(greeting)):
    print(i,greeting[i])

for i in range(0, len(greeting)):
    print(f"The character is {greeting[i]} is at index {i}")

for index, item in enumerate(greeting):
    print(f"The character is {item} is at index {index}")

name ='PRAMOD'
for i, j in enumerate(name):
    print(f"The character is {j} is at index {i}")

#Python code to reverse the text
text = 'PRAMOD MAHARAJ'
reverse = text[::-1]
print(reverse)



