# Handling with csv file
import csv

# Handling Bad records in csv file.

total = 0.00
# Open and read the CSV file
with open("C://Users//Sanjiva//Desktop//portfolio.csv") as file:
    next(file, None)  # Skip the header, but here not need
    rows = csv.reader(file)
    for row in rows:
        try:
            total += int(row[1])
        except ValueError as err:
            print(f"Error in rownumber:, {row[0]}, :, {err}")


print('Total value of stock is :', total)
