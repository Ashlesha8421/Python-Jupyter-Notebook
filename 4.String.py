# Python String:
''' Strings are sequences of characters. Yor name is also string.'''

# How to create a string and assign it to a variable :
"""To create a string, put the sequence of characters inside either single quotes, double quotes, or 
triple quotes and then assign it to a variable."""

Single_quote_character = 'a'
print(Single_quote_character)

print(type(Single_quote_character)) # check the type of the variable.

# Similarly, you can assign a single character to a variable double_quote_character.
double_quote_character = "b"

print(double_quote_character)
print(type(double_quote_character)) # check the type of the variable.

# Also check out if you can assign a sequence of characters or multiple characters to a variable.

double_quote_multiple_characters = "aeiou"
single_quote_multiple_characters = 'aeiou'
print(type(double_quote_multiple_characters),type(single_quote_multiple_characters))

# Also used triple quote
triple_quote_example = """this is a sentence written in triple quotes"""
print(type(triple_quote_example))


# String common methods:
# 1.Get the index of a substring in a string.

# find the index of a "c" in a string "abcde"
print("abcde".index("c"))

'''2 is returned because the position of the individual letters in the strings is 0-indexed. 
So, index of "a" in "abcde" is 0, that of "b" is 1, and so on.'''

# Test if a substring is a member of a larger string.
# This is done by using "in" keyword.

"""for example, test if string "i" is present in string "pythonic" at least once. 
"i" is present in the string. Therefore, the result should be true."""

print("i" in "pythonic")
print("k" in "pythonic")

# Join a list of strings using the join method.
"""A list of strings is written by delimiting the sequence with a comma ,, 
and enclosing the whole group with brackets [...]. For a more detailed tutorial on lists head over 
to the python lists tutorial. You can join a list of strings by giving the delimiter as the object on 
which the method join will act and the list of strings as the argument."""


# JOIN
# join a list of strings 1, 2, 3 with a space as a delimiter and 1,2,3 as the list of strings.
# So, the result will be the strings with spaces between them.
join = (' '.join(['1','2','3']))
print(join)

#BREAK
# Break a string based on some rule.
# This takes in the string as the object on which the method split is passed using the dot operator.
# Splitting takes a space as the default parameter.

# split the string "1 2 3" and return a list of the numbers.
k = "1 2 3".split() # splitting
print(k)

# Or you can split a string based on a delimiter like :.
k = "1:2:3".split(':') # splitting
print(k)

# ACCESS individual Character in string
lang = "python"
print(lang[0]) # access 1st element
print(lang[2]) # access 3rd element

# Formatting in String:
# .format method
'''String object can be formatted. You can use %s as a formatter which will enable you to 
insert different values into a string at runtime and thus format the string. 
The %s symbol is replaced by whatever is passed to the string.'''

print("I love %s in %s" % ("programming", "Python")) # templating strings

# You can also use the keyword format. This will enable you to set your own formatters instead of %s.
print("I love {} in {}".format("programming","Python"))

# Truth value testing of String

# A string is considered to be true in Python if it is not an empty string. So, we get the following:
print(bool(""))
print(bool("x"))
print(bool(" "))

# Hope You Like This :)
# THANK YOU




