#Comma Separated File(CSV)
import csv
#This Program read CSV file and prints contents

with open("Test.csv",) as csvfile:
     reader = csv.reader(csvfile)
     for col in reader:
         print(col[0], col[1], sep="||")