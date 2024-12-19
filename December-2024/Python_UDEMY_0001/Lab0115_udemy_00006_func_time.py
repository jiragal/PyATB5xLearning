# This program will calculates time taken by the function
import time


def time_taken(*args, **kwargs):
    # Save time stamp
    start = time.time()
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs)
    end = time.time()
    print(end - start)


find_time = time_taken('Hello', 'Welcome', 'to', 'GeeksforGeeks', s1='Geeks', s2='for', s3='Geeks')
print(find_time)
