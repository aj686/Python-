# BASIC LEARNING


#---------BASIC SYNTAX---------------

# simple syntax
print("Hello Ajwad")

# variable in python 
x = "c++"      
y = 'JS'
z = 100

# Error syntax


#---------PYTHON COMMENT------------- 

# This comment is for one lie

'''
This comment more than one line
'''

#----------VARIABLES-------------------
# Variable is assign a value to it (declaration)
# can use double or single quotation 
# variable create outside of function "GLOBAL VARIABLE"
# rule for VARIABLE NAME is
'''
- START WITH LETTER 
- CANNOT START WITH NUMBER
- CONTAIN ALPHA-NUMERIC CHARACTERS AND UNDERSCORES (A-z, 0,-9 and_)
- CASE-SENSETIVE (Age, age are different variable)
'''

'''
SYTLE CREATE VARIABLE NAME
1. CAMEL CASE   myVariableName = "John"
2. PASCAL CASE  MyVariableName = "John"
3. SNAKE CASE   my_variable_name = "John"
'''

variablename ="This is string" #string data type
number = 12345 #integer data type
print(variablename)
print(number)

# to specify the data type
a = str(1)      # output '3'
b = int(12)     # output 3  --->without decimal point
c = float(12)   #output 3.0 ---> with decimal point

# Get data type from variable with print 
print (type(a))  # <class 'str'>
print (type(b))  # <class 'int'>

# Case-sensetive
# python can differentship the variable even a and A
a = "CSS"
b = "HTML"

# Multiple variable with multiple value
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Multiple variable with one value
x = y = z = "Orange"
print(x)
print(y)
print(z)

# can use LIST or TUPLE to store a data into variable
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# combine out both text and vaiable use '+'
v = "Y15"
print("I like" + v)

# add variable with other variable
v = "Y15"
m = "Yamaha"
print(m + v)

# GLOBAL VARIBALE is variable outside of function
# globl variable
R = "JS is one of programming language"
# defined function name
def language():
    print("I like" + R)
# call function name
language()

# LOCAL VARIBALE is variable inside of function
R = "JS is one of programming language"
# defined function name
def lang():
    r = "Java"
    print("I like" + r) #inside function
# call function name
lang()

print("I like" + R) #outside function