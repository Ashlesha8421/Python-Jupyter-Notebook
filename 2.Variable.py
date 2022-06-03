# Variables

# Variable is nothing but Storage container for data.
# Every variable will have a name.
#  for example , Pi=3.14 , here we assign some value to pi variable.

variable_name = "Hello World"
print(variable_name)

# assign the value 299792458 to the variable speed_of_light
speed_of_light = 299792458
print(speed_of_light)

# assign a decimal number 3.14 to the variable pi
pi = 3.14
print(pi)

# assign a string
fav_Lag = "Python"
print(fav_Lag)

# Valid and invalid ways of assigning variables:
# 1.If you have more than one word in the name then use " _ " ;otherwise it gives SyntaxError.
# multiple words = "World"
# print(multiple words) # it gives SyntaxError: invalid syntax

multiple_word = "multiple word"  # note the variable name has an underscore _
print(multiple_word)

# 2.DO NOT START WITH NUMBER.
# You can't start a variable name with a number. The rest of the variable name can contain a number.
# For example, 1var is wrong.
# 1Var = 1234
# print(1Var)  # it gives SyntaxError: invalid syntax

Var1 = 123
print(Var1)

# 3.More points to remember while deciding a variable name
# You can only include a-z, A-Z, _, and 0-9 in your variable names. Other special characters are not permitted.
# For example, you cannot have hash key # in your variable names.

# a_var_containing_# will not work as it has # in the name
# a_var_containing_#  = 1
# print(a_var_containing_#) # it gives SyntaxError: unexpected EOF while parsing

# Interestingly, you can have a variable name in your local language.
零 = 0 # chinese
print(零)

ශුන්ය = 0 # sinhala
print(ශුන්ය)


# MORE ON ASSIGNING
# Python supports assigning all data structures to variables.

# 1. assigning list
my_list = ["Elon Musk","Ratan Tata"]
print(my_list)

# 2.assigning Dict
Birthday ={"Mom":"3may","Dad":"8oct"}
print(Birthday)


# 3.assigning functions
import functools
memoize =functools.lru_cache
print(memoize)

# 4.assigning Class
class MyClass:
    pass

give_me_more =MyClass()
print(give_me_more)


# Working with variables
# Variables will support any method the underlying type supports.
# For Example,if an integer value is stored in a variable, then the variable will support integer functions such as addition.

Var = 2
print(Var * 3)
print(Var/8)
print(Var + 5)
print(Var - 9)
print(Var//3)

# You can make a change in a variable and assign it to the same variable.
# This is done generally when some kind of data type change is done
# For example, you can take a number as input.This will take in the digit as a string.
# You can then take the string number and convert it to int and assign it to the same number.

# number = input()
# print(type(number)) # it gives str

print(range(5))

id1,id2,id3 =range(3)
print(id1)
print(id2)
print(id3)


# Hope You Like This :)
# Thank You


