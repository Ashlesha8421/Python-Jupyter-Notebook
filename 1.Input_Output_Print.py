# Python Input and Output

# Input using the input( ) function
raw = input()

# Output using the print() function
'''To output your data to the screen, use the print() function. You can write print(argument) 
and this will print the argument in the next line when you press the ENTER key.'''

print('Python')

# More on using input
# take an input and assign it to a variable
beautiful_number = input()
print(beautiful_number)

# Give a helpful hint during the prompt
beautiful_number =input("Tell me beautifule number".format(beautiful_number))
print(beautiful_number)


# More on using print
'The (asterisk) * operator performs repetition on strings. You can print "5" six times. '
print("5"*6)

'You can separate the output using the comma delimiter. By default, this adds a space between the output items.'
print(5,6,7)


'''To change the output to what you want, use the keyword arguments sep and end to print ( ). 
When separating the output with a comma delimiter,you can also define the separation format using the sep keyword.'''
print(5,6,7, sep=",")

'By default, print goes to a new line at the end. You can change this by using the keyword end '
print(5,6,7,sep=",",end="!!!!!....")

# For example, you can print the letters in the word "python" and all the letters will come in a new line.
for i in "Python":
    print(i)

# You can change this default implementation. You can have a colon : between the letters instead of a new line.
for i in "Python":
    print(i,sep=":")


# Printing the result of a calculation
'''assign the number 7 to a variable population and if you write the logic population * 7 inside 
the parentheses of print, it will just do the calculation up front and print the result.'''

population = 9
print("Population result in 2012:",population*1.25)







