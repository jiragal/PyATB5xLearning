import pandas as pd
#pandas is used for data manipulation
#openpyxl is used as engine for reading and writing Excel files
#Load the Excel file
input_file=r'D:\DELL DATA\Documents\PavanKumar_Python\Day25-DataDrivenTesting_Excel\ClassExamples (2)\ClassExamples\data.xlsx'
# File--->WorkBook--->Sheets--->Rows--->Cells
workbook= pd.read_excel(input_file)
# print("Original Data")
# print(workbook.head())
# print(workbook.columns)     #print only column name
#
# print(workbook['Location'])
#print(workbook.loc[0]) # Access data by row label (index)
# print(workbook.iloc[1]) #Access data by row number
# print(workbook.loc[0, 'BookName']) # access a specific cell
# print(workbook.iloc[0, 0])  # access a specific cell

#Iterate over rows
for index, row in  workbook.iterrows():
    print(row["BookName"])
