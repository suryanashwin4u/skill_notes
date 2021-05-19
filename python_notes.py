                python notes
==================================================

It was created by Guido van Rossum

--------------------------------------------------
# to check version of python from command prompt
python --version

--------------------------------------------------
# to run python file at command prompt
python file.py

--------------------------------------------------
# type python to run python editor at command prompt
python 

or

py

--------------------------------------------------
# type exit() to come out of cmd editor
exit()

--------------------------------------------------
# multiline comments in python
'''helloworld
aklakakkada
akalkjakja
aslkjladskj'''

--------------------------------------------------
# variables in python

x = 4       # x is of type int
x = "Sally" # x is now of type str

--------------------------------------------------
# casting in python

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


--------------------------------------------------
# get type of variables

print(type(x))
print(type(y))

--------------------------------------------------
# string can be enclosed in single or double quotes

x = "John"
# is the same as
x = 'John'

--------------------------------------------------
# variables are case sensitive

a = 4
A = "Sally"
#A will not overwrite a

--------------------------------------------------
# type of variables we can declare in python


# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


--------------------------------------------------
# camelcase declaration

myVariableName = "John"

--------------------------------------------------
# pascal case declaration

MyVariableName = "John"

--------------------------------------------------
# snake case variable declaration

my_variable_name = "John"
--------------------------------------------------
# different variable assignments in python

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

--------------------------------------------------

# same variable assignments in python

x = y = z = "Orange"
print(x)
print(y)
print(z)
--------------------------------------------------
# list items to variable assignment

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

--------------------------------------------------
# variable as output using plus operator

x = "awesome"
print("Python is " + x)

--------------------------------------------------

# addition using plus operator
x = 5
y = 10
print(x + y)

--------------------------------------------------
# x is a global variable

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

--------------------------------------------------
# x is global here

x = "awesome"

def myfunc():
  # x is local here
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

--------------------------------------------------
# x is declared global forcefully inside function scope

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

--------------------------------------------------
# use global keyword to change the value inside function

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


--------------------------------------------------

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview


x = "Hello World"               	            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                    bool	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview



x = str("Hello World")	                        str	
x = int(20)	                                    int	
x = float(20.5)	                                float	
x = complex(1j)	                                complex	
x = list(("apple", "banana", "cherry"))	        list	
x = tuple(("apple", "banana", "cherry"))	    tuple	
x = range(6)	                                range	
x = dict(name="John", age=36)	                dict	
x = set(("apple", "banana", "cherry"))	        set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	                                    bool	
x = bytes(5)	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview	


--------------------------------------------------
# int type
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
--------------------------------------------------
# float types
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
--------------------------------------------------
# complex types
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


--------------------------------------------------
# type conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note: You cannot convert complex numbers into another number type.

--------------------------------------------------
# to output a random number between given range

import random
print(random.randrange(1, 10))
--------------------------------------------------
# convert types

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

--------------------------------------------------
# string can be single or double quotes

print("Hello")
print('Hello')

-------------------------------------------------
# multiline string

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

------------------------------------------------
# get   character at position 1

a = "Hello, World!"
print(a[1])


------------------------------------------------
# looping thru every character in a string

for x in "banana":
  print(x)


------------------------------------------------
# check the length of the string

a = "Hello, World!"
print(len(a))

-----------------------------------------------

# to check string in a long string

txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")
-----------------------------------------------
# to return a range of characters from a string

b = "Hello, World!"
print(b[2:5])


b = "Hello, World!"
print(b[:5])


b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

----------------------------------------------
# change into upper case

a = "Hello, World!"
print(a.upper())

---------------------------------------------------
# change into lower case

a = "Hello, World!"
print(a.lower())

---------------------------------------------------

# remove space around string

a = " Hello, World! "
print(a.strip())

---------------------------------------------------
# replace string characters

a = "Hello, World!"
print(a.replace("H", "J"))

---------------------------------------------------

# split into list

a = "Hello, World!"
print(a.split(",")) 

----------------------------------------------------

# change only first letter of the string to uppercase

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

----------------------------------------------------

# similar to string.lower() but more powerfull

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


-----------------------------------------------------
# to align txt into center taking up 20 spaces

txt = "banana"
x = txt.center(20)
x = txt.center(20, "O") #fill O in spaces
print(x)

-----------------------------------------------------

# return number of string matching

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
x = txt.count("apple", 10, 24) #start search from 10th and ends at 24th position
print(x)

-----------------------------------------------------

# UTF-8 encode by default

txt = "My name is Ståle"
x = txt.encode()
print(x)

# 'strict'	- Default, raises an error on failure

# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
print(txt.encode(encoding="ascii",errors="backslashreplace"))

# 'ignore'	- ignores the characters that cannot be encoded
print(txt.encode(encoding="ascii",errors="ignore"))

# 'namereplace'	- replaces the character with a text explaining the character
print(txt.encode(encoding="ascii",errors="namereplace"))

# 'replace'	- replaces the character with a questionmark
print(txt.encode(encoding="ascii",errors="replace"))

# 'xmlcharrefreplace'	- replaces the character with an xml character
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

--------------------------------------------------------

# return true or false
txt = "Hello, welcome to my world."

# ends with dot
x = txt.endswith(".")

# ends with text
x = txt.endswith("my world.")

# check the ending text from the given position
x = txt.endswith("my world.", 5, 11)

print(x)

--------------------------------------------------
# give spaces between each character where \t is given

txt = "H\te\tl\tl\to"
# Default tabsize is 8
x =  txt.expandtabs(2)
print(x)


txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

-------------------------------------------------
# return location of the text
txt = "Hello, welcome to my world."
x = txt.find("welcome")
x = txt.find("e")

# start and ending search position
x = txt.find("e", 5, 10) 

# If the value is not found, the find() method returns -1, but the index() method will raise an exception
print(txt.find("q"))
print(txt.index("q"))

print(x)

-------------------------------------------------
# 2 digits of decimals
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

-------------------------------------------------

#setting space to 8 characters and Use ">" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49))


#setting space to 8 characters and Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))

#setting space to 8 characters and Use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))

#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

#Use "+" to always indicate if the number is positive or negative:
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))


#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))


#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))


#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old."
print(txt.format(13800000000))


#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))


#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))


#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101))

#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5))


#Use "E" to convert a number into scientific number format (with an upper-case E):
txt = "We have {:E} chickens."
print(txt.format(5))


#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))


#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))


#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))


#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))


#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))


#Use "X" to convert the number into upper-case Hex format:
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))


#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))












































































-------------------------------------------------
# returns true or false
print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

------------------------------------------------
# returns true or false 
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# return True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


----------------------------------------
# return false using oop

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
----------------------------------------
#function return True 
def myFunction() :
  return True
print(myFunction())

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")


-------------------------------------------------
# check if an object x instance of of int class

x = 200
print(isinstance(x, int))

------------------------------------------------

# +	Addition	            x + y	
# -	Subtraction	            x - y	
# *	Multiplication	        x * y	
# /	Division	            x / y	
# %	Modulus	                x % y	
# **	Exponentiation	        x ** y	
# //	Floor division	        x // y	

------------------------------------------------

# =   	  x = 5	      x = 5	
# +=	    x += 3	    x = x + 3	
# -=	    x -= 3	    x = x - 3	
# *=	    x *= 3	    x = x * 3	
# /=	    x /= 3	    x = x / 3	
# %=	    x %= 3	    x = x % 3	
# //=	    x //= 3	    x = x // 3	
# **=	    x **= 3	    x = x ** 3	
# &=	    x &= 3	    x = x & 3	
# |=	    x |= 3	    x = x | 3	
# ^=	    x ^= 3	    x = x ^ 3	
# >>=	    x >>= 3	    x = x >> 3	
# <<=	    x <<= 3	    x = x << 3
# ==	  Equal	                        x == y	
# !=	  Not equal	                    x != y	
# >	    Greater than	                x > y	
# <	    Less than	                    x < y	
# >=	  Greater than or equal to	    x >= y	
# <=	  Less than or equal to	        x <= y

-----------------------------------------------------

# and    	Returns True if both statements are true	x < 5 and  x < 10	
# or	    Returns True if one of the statements is true	x < 5 or x < 4	
# not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

-----------------------------------------------------

# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

-----------------------------------------------------
# &   	AND	Sets each bit to 1 if both bits are 1
# |	    OR Sets each bit to 1 if one of two bits is 1
#  ^	  XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	  NOT	Inverts all the bits
# <<	  Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	  Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off



----------------------------------------------
# concatenate string

a = "Hello"
b = "World"
c = a + b
print(c)

# space concatenate
a = "Hello"
b = "World"
c = a + " " + b
print(c)

-----------------------------------------------
# use format function to concatenate integers numbers in the string

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



----------------------------------------------------
# escape characters

# \'	    Single Quote	
# \\	    Backslash	
# \n	    New Line	
# \r	    Carriage Return	
# \t	    Tab	
# \b	    Backspace	
# \f	    Form Feed	
# \ooo	    Octal value	
# \xhh	    Hex value

txt = "We are the so-called \"Vikings\" from the north."


-----------------------------------------------------
# making list and printing
# List items are ordered, changeable, and allow duplicate values.

thislist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]

# check length of the list
print(len(thislist))

# check datatype of list
print(type(mylist))

# access list items
print(thislist[1])

# access last item
print(thislist[-1])

# access items in range index:2 to 4
print(thislist[2:5])

# access items in range index:0 to 3
print(thislist[:4])

# access items in range index:2 to end
print(thislist[2:])

# access items in range index:-4 to -2
print(thislist[-4:-1])

# check item in the list or not
if "apple" in thislist:

# change item of a list
thislist[1] = "blackcurrant"  

# change many items of a list
thislist[1:3] = ["blackcurrant", "watermelon"]

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# insert at 3rd position in the list
thislist.insert(2, "watermelon")

# add at the end of the list
thislist.append("orange")

# add 2 list or tuple to the list together
thislist.extend(tropical)

# to remove item from a list
thislist.remove("banana")

# to pop up item from the given index of the list
thislist.pop(1)

# to pop up from the end
thislist.pop()

# remove the first item from the list
del thislist[0]


# delete the entire list
del thislist

# clear the list 
thislist.clear()

--------------------------------------------------

# loop through a list
for x in thislist:
  print(x)

# loop thru a list having some length and print the items
for i in range(len(thislist)):
  print(thislist[i])

# loop thru a list having some length and print the items
while i < len(thislist):
  print(thislist[i])

# shorthand loop items printing with next line
[print(x) for x in thislist]

# to check character and add into new list using loop
for x in fruits:
  if "a" in x:
    newlist.append(x)

# to check character and add into new list using loop
newlist = [x for x in fruits if "a" in x]

# make a new list of items in fruits other than apple
newlist = [x for x in fruits if x != "apple"]

# make a new list of items carring all items in a fruit
newlist = [x for x in fruits]

# make a new list of items carring all numbers from 0 to 9
newlist = [x for x in range(10)]

# make a new list of items carring all numbers less than 5
newlist = [x for x in range(10) if x < 5]

# make a new list of items using uppercase
newlist = [x.upper() for x in fruits]

# make a new list of items having 'hello'
newlist = ['hello' for x in fruits]



# convert a tuple into list
thislist = list(("apple", "banana", "cherry"))

# List:ordered and changeable. Allows duplicate members.
# Tuple:ordered and unchangeable. Allows duplicate members.
# Set:unordered and unindexed. No duplicate members.
# Dictionary:ordered* and changeable. No duplicate members.




