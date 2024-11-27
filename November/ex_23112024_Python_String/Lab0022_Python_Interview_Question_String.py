#To find non repetative character from the String
def find_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(find_char("swiss"))
print(find_char('dada'))
print('pepper')
print('annusinha')