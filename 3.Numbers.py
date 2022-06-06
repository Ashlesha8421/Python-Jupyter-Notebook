# WHAT ARE NUMBERS IN PYTHON ?
"""All numbers that are handled will belong to some type
A type is a way to define various data structures and containers and define the functionality associated with them.
Types are implemented in Python as classes.

If you want to verify if an integer belongs to the class int you can use isinstance.
You will need to pass number as the first argument and class name as the second argument, and it will check if the object is an instance of the class.
This is done by the following construct. """


#isinstance(object, class)

isinstance(5, int)  # return 0 means TRUE

# Numeric types and operations using numbers :
""" There are 3 numeric types in python
1. int fot Integer
2. float for Decimal Numbers
3. complex for Complex Numbers """

# assign the integer 2 to a var int_var
int_var = 2

# assign the integer 3 to a var int_var1
int_var1 = 3

# print the sum of the two variables int_var and int_var1
print(int_var + int_var1)

""" Similarly, assign two decimal numbers to two variables, say, float_var1 and float_var2,
 and print the sum of the two """

# assign a decimal number to a variable float_var
float_var =5.6

# assign a decimal number to a variable float_var1
float_var1 = 6.7

# print the sum of the two decimal numbers
print(float_var + float_var1)

"""Similarly for Complex numbers"""

# assign a complex number to a variable complex_var
complex_var = (5 + 3j)

# assign another complex number to a variable complex_var1
complex_var1 = (4 + 9j)

# print the sum of the two complex numbers
print(complex_var + complex_var1)

# In case of division, dividing two integers will always result in a float.
result = 3/8
print(result)

isinstance(result,float)

"""Operations between numbers of different types: 
The operations work when operate of variables that are of different numeric types as well."""

# add two numbers, one is int and the other is float
result = 2 + 3.3
print(result)
isinstance(result,float)

"""Other operations like adding int to complex or float to complex works in similar manner. 
The results of both the operations belong to the complex class."""

# add two numbers belonging to complex and int class
result = (3 + 2j)+5
print(result)

# check if the result is of class complex
print(isinstance(result, complex))

# add two numbers belonging to complex and float class
result = (5 - 8j) + 1.2j
print(result)

# check if the result is of class complex
print(isinstance(result, complex))


























