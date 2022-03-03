# All about Strings

# What is a strong?
# A String is a sequence of characters. I t can be difined with
# either single or double quotes.
# single quotes.
alpha = 'Hello'


# double quotes
beta = "python"

# print results
print(alpha)
print(beta)

# A multi-line strong uses three single or three double quotes
# and allows a string to be created on multiple lines.
multi = '''This string can be seen
on multiple lines so you could do paragraph if you wanted'''
print(multi)

# getting a specific index using the square bracket []
charlie = 'Happy'
print(charlie[2])

# if you put in a value of the index that is higher than the number of
# characters -1 you will generate an error
# print(charlie[5])

# slicing and range of characters
# using the sae square brackets, you can output a range of characters
# from a strong. This is called slicing. You use a colon to serperate the
# start and end of the slice.
delta = 'Enjoy Python'
print(delta[2:5])
# output should be joy

# negative slicing we use negative numbers. Instead of starting from zero
# it begins at the end of the string
print(delta[-5:-2])
# output should be yth

# What is a check string
# This technique is the ability to compare a set of characters ith a strong
# variable. This result wll be either True or False. We use in or not in
# keywords for check string
# using the in keyword
txt= 'This is a test sentence'
result1= 'is' in txt

# using the not in kewprd
txt2 = 'This other prhase is also a test'
result2 = 'th' not in txt2

print(result1)
print(result2)

# String concatenation in Python is the ability to join 2 or more strings
# using the plus operator.
# Basic concatenation
cat1= "Happy"
cat2= "Friday"
combine = cat1 + cat2
print(combine)
combine2 = cat1 + " " + cat2
print(combine2)

cat3 = 'Sample'
combine3 = cat3 + ' Code'
print(combine3)

# longer concatenation with more than 2 values
combine4 = cat1 + ' ' + cat2 + ' ' + combine3
print(combine4)

# What about strings and a number
# combine5 = cat3 + 5
# print(combine5)

# basic strong format method using only a curly brace
age = 4
msg1 = ' My dog is {} years old'
print(msg1.format(age))

# string format using indexing
msg2 = 'my dog {1} is {0} years old'
print(msg2.format(age, 'Spot'))

# Optional format
name = 'John'
total = 34.9856
msg3 = 'Hello {0}, you order comes to {1:6.2f}'
print(msg3.format(name, total))

# octal escape sequence '\110\145\154\154\157'
value_0 = '\110\145\154\154\157'
print(value_0)

# Escape Sequence allows you to use characters that are reserved using
# bachslash
value_more = 'That\'s a cool toy. \tcan I\n play with it?'
print(value_more)

# String methods are methods built in to python
value_string = ' Hello, World '

#strip()
print(value_string.strip())

# lower()
print(value_string.lower())

# upper()
print(value_string.upper())

# replace()
print(value_string.replace('e', 'a'))

# split()
print(value_string.split(','))

value_more = 'hello python'

# capitalize()
print(value_more.capitalize())

value_upper = 'PYTHON'

# casefold()
print(value_upper.casefold())

# centered()
print(value_more.center(40))


