# List Comprehensions:
# It is very easy and compact way of creating list objects from any iterable objects(like
# list,tuple,dictionary,range etc) based on some condition.
# Syntax:  list=[expression for item in list if condition]

# If you want to store squares of numbers form 1 to 10 in a list,
list1 = []
for item in range(1, 11):
    list1.append(item)
print(list1)
#List Comprehensions : way
list_numbers = [item for item in range(1,11)]
print(list_numbers)

#Square Numbers in the range(1,11)
l1 = [x * x for x in range(1, 11)]
print(l1)

# List of even numbers between range 1-50
ev1 = [item for item in range(1,51) if item%2 == 0]
print(ev1)

# Returns a list containing all vowels in the given string
list1 = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex','evilia','anup','ivan','om']
vowel_names = [name for name in list1 if name[0].lower() in "aeiou"]
print(vowel_names)

# Filtering all the languages which starts with 'p'
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Pascal','Pega','Cobol']
p_languages = [ item for item in languages if item.lower().startswith('p')]
print(p_languages)
#Another way
p_list = [item for item in languages if item.lower()[0]=='p']
print(p_list)