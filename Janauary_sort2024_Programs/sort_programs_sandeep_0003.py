# import pytest
# import allure


def sort_temperature(item):
    return item[-1]


temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 38), ('Rajasthan', 45)]

# Using Normal function
temp_sort = sorted(temperatures, key=sort_temperature)
print(temp_sort)

# 2nd way is use Lambda function
lambda_method = sorted(temperatures, key=lambda item: item[-1])
print(lambda_method)
