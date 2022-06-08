# Python Control Structures - Loops and Conditionals

"""You can control the flow of logic in your code through various methods.

* Basic control flows
1.Selection (if statements)
2.Iteration (for loops)

* More advanced control flows
1.Procedural Abstraction (functions)
2.Recursion
3.Concurrency
4.Exception Handling and Speculation
5.Nondeterminacy

* How to have 'sequential, selective and iterative flows' in your code.
This can be achieved using the for 'loop'.

* How to 'achieve procedural abstraction'.
 This can be done by the use of 'functions'."""

# Loops
# Working on items of the iterable

"""If you want to run an operation on a collection of items, then you can do it using for loops.
The skeleton for using the for loop is shown below.
"""

# Points to Note
"""1). The for statement line will end with a colon :
   2). The rest of the code block must be indented with a spacing of 4 spaces.
   3). An iterable is any object that can be looped on such as list, tuple, string etc.
"""

''' 
for item in iterable: # you can place any list or tuple or string in place of iterable
    #Write code here
    pass 

'''
# If you want to print an element of a list of fruits,
fruits=["Mangoes","Apples","oranges"]

for fruit in fruits:
    print(fruit)

'''In the example above, note that items in the iterable (i.e fruits) will be assigned to the for 
loop variable (i.e fruit) during the iteration process.So, we can access the item directly. '''

for fruit in fruits:
    string_size = 0
    for alphabate in fruit:
        string_size += 1
    print("name of fruit: {} is has length {}".format(fruit,string_size))


# Looping on both indexes and items
"""index or the place value of the item in the iterable was not considered. 
However, if you are interested in working with the index, then you can call the 'enumerate function'
which returns a tuple of the index and the item."""

for index,fruit in enumerate(fruits):
    print("index is %s" % index)
    print("fruit is %s" % fruit)
    print("--------------------")

# While statement
""" The while statement will execute a block of code as long as the condition is true. 
The skeleton of a while block is shown below. 

while condition:
    code_block
    
1).Note that similar to the for loop, the while statement ends with a colon :
2).The remaining code block is indented by 4 spaces.
3).We can implement the fruit example in the while block as well, although the logic becomes 
a bit complicated than the for block.
    
"""
fruits = ["apples", "oranges", "mangoes"]  # TO GET THE LIST
length = len(fruits) # get the length that we required in
i = 0 # intialise a counter
while i < length: # the given condition
    print(fruits[i]) # the code block
    i += 1 # increment the counter


# Nested for loops
# You can have one or more nested for loops.

for i in range(1,5):
    for j in range(1,5):
        print('%d * %d = %d',(i,j,i*j))



# Selection and Python If statements
# Creating if blocks

'''if condition1:
    code_block1
    
elif condition2:
    code_block2
    
else:
    code_block3'''

# For example :
num = 42
if num == 42:
    print("number is 42")

num = 45
if num == 42:
    print("nummber is 42")
else:
    print("number is not 42")

num = 45
if num == 42:
    print("number is 42")
elif num == 44:
    print("number is 44")
else:
    print("number is neither 42 or 44")

# Nested if statements
num = 35.8
if num > 20:
    if num < 50:
        print("number between 20 and 50")





















































