from November.ex_05112024_Python_Basics.Lab001_Python_Helloworld import sentence, languages

# this is called immutability of strings
# strings are immutable. Meaning once the strin is created, you cannot change the value of the string

print('Hello World')
greet = 'Hellow how are you'
print(greet)
sentence = 'hello world welcome to python'
languages = "'Python','Cobol','Rubby','C','C++','C-sharp'"
print(sentence)
print(languages)
# type is used to get the datatype of a variable
tpe = type(greet)
print(tpe)
num1 = 10
num2 = 10.00
num3 = True
print(num1, num2, num3)
print(type(num1), type(num2), type(num3))

# triple quotes are used as documentation strings in functions
# triple quotes are used to represent a multi-line string

paragraph = """Hello world
    welcome to python
             Python is object oriented language"""
print(paragraph)
print(type(paragraph))
print(len(paragraph))  # Here we have used length command
# len is an inbuilt function used to get the length of the string!
name = "Pramod"
name = 10
print(name)
name = True
print(name)
print(type(name))

name = 10.5
print(type(name))

name = [1, 2, 3, 4]
print(type(name))

name = ('sanjiva', 'pramod')
print(type(name))

word = ''
print(type(word))

word = 'hello'
word1 = 'HELLO I LOVE YOU'
print(word.upper())
print(word1.lower())
print(len(word))
print(word.count('l'))
sentence = 'hello world hello hello hello universe hi there hi how are you doing'
print(sentence.count("hello"))

# Very important one "dir" will let you what are all the options are there in string
print(dir(word))
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# zfill only works with string not integer
c = 10
d = str(c)  # I am converting this to str
word2 = 'Python'
Sentence1 = "Hello how are you boss what is your next plan"

print(d.zfill(10))
print(word2.zfill(10))

# 2nd: The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# string.split(separator, maxsplit)
x = Sentence1.split(' ')
print(x)
my_list = "'Alex','Ronald','John'"
my_list = my_list.split(',')
print(my_list)

my_list = "'Alex','Ronald','John'"
my_list = my_list.split(',', 1)
print(my_list)

text = "apple orange banana"
fruits = text.split()
print(fruits)

# 3rd casefold() Change to lower case for all upper case chars in a string
name = "PRAMOD"
print(Sentence1.casefold())
print(name.casefold())
my_str = "aBcßeF"
print(my_str.casefold())
print(my_str.lower())
# Use Case: Normalizing Input for Case-Insensitive Search
# Use casefold() to normalize input for a search function, allowing for accurate case-insensitive
search_term = "PYTHON"
content = "Learning python programming."
if search_term.casefold() in content.casefold():
    print("Search term found!")
else:
    print('Not found')

line = "        hello world    "
print(line.strip())  # Here we are using strip & # strips leading and trailing white spaces
_word = 'hello world wellcome'

print(_word.endswith('world'))
print(_word.endswith('wellcome'))
print(_word.startswith('hello'))

my_list = ['Alex', 'Ronald', 'John']
output = ' '.join(my_list)
print(output)

# join(): Joining string
# By using join() we are creating strings.
lst1 = ['Pramod', 'Gunda', 'Dutta']
output = " ".join(lst1)
print(output)

my_string = 'hello'
print('@'.join(my_string))

my_tuple = ('Alex', 'Bob', 'Washington')
print(' '.join(my_tuple))

# very very important string functions
# 1. split()
# 2. join()
# 3. strip()
# 4. endswith()
# 5. startswith()
# 6. count()
# 7. zfill()
