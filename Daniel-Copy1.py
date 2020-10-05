#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 1
y = 2
z = 3


# In[2]:


x + y + z


# In[3]:


def add_numbers (x,y):
    return x * y
add_numbers (1,2)    


# In[4]:


def add_numbers(x,y,z = None):
    if (z == None):
        return x + y
    else:
        return x + y +z
print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))


# In[5]:


def add_numbers (x, y, z = None, flag = False):
    if (flag):
        print('Flag is true!')
    if (z == None):
        return x + y
    else:
        return x, y, z
    
print(add_numbers(1, 2, flag = True))


# In[6]:


def add_numbers(x, y):
    return x + y

a = add_numbers
a (1, 2)


# In[7]:


x = ('daniel', 1 , '!', 'x')
type (x)


# In[8]:


z = ['daniel', 1, 'x']
type (z)


# In[9]:


z.append(3.3) # I have invocated some many times, that's why the answer
print(z)


# In[10]:


ages = input("How old are you? ")

age = int(ages)

seconds = age * 365 * 24 * 3600
strsec = str(seconds)

print("you have lived for" + strsec + "seconds ")


# In[11]:


def live_seconds(x, y, z = None):
    if (z == None):
        return x + y
    else:
        return x + y + z
print(live_seconds(1, 2))
print(live_seconds(1, 2, 3))    
      


# In[12]:


ages = input("How old are you? ")
age = int(ages)
seconds = age * 365 * 24 * 3600

strsec = str(seconds)

print("You have lived for " + strsec + " seconds")


# In[13]:


birth = input(" When did you born? ") # pendent to get the number of days or hours or seconds from the day I was born to this day
day = int(birth)

if year == 12
    return 


# In[14]:


def add_numbers (x, y, z = None):
    if z == None:
        return x + y
    else:
        return x + y + z
print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))


# In[15]:


def add_numbers (x, y):
    return x + y

add_numbers(1, 2)


# In[16]:


def add_numbers (x, y, z = None, flag = False):
    if flag:
        print ("Flag is True")
    if z == None:
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag = True))


# In[17]:


def add_numbers (x, y):
    return x + y

a = add_numbers
a(1, 2)


# In[18]:


type(a)


# In[19]:


x = (1, "daniel", 'b', 3)
type(x)


# In[20]:


print(x)


# In[21]:


y = [2, 'Hernando', "c", 4]
type (y)


# In[22]:


print(y)


# In[23]:


y.append(3.3)
print(y)


# In[24]:


for item in y:  # this a list
    print(item)


# In[25]:


for item in x:  #this is a tuple
    print(item)


# In[26]:


len(x)


# In[27]:


y[0]


# In[28]:


i = 0
while( i != len(x)):
    print(x[i])
    i = i + 1


# In[29]:


y [2]*3


# In[30]:


x + y


# In[31]:


y


# In[32]:


4 in y


# In[33]:


x


# In[34]:


3 in x


# In[35]:


x[0:3]


# In[36]:


y[0:2]


# In[37]:


y[-1]


# In[38]:


x.append (3.3)


# In[39]:


z = [78, "Bernal", '$5']
type(z)


# In[40]:


i = 0
while i != len (z):
    print(x[i])
    i = i + 1    


# In[41]:


y + z


# In[42]:


a = (56, 'hello')
b = ("dude", 38)


# In[43]:


a + b


# In[44]:


a * 3


# In[45]:


56 in a


# In[46]:


x [1:2]


# In[47]:


x [-4:-2]


# In[48]:


x


# In[49]:


x [-3:-1]


# In[50]:


x[:3]


# In[51]:


y


# In[53]:


y.append(5.2)


# In[54]:


y


# In[55]:


y[3:]


# In[56]:


firstname = 'Daniel'
lastname = "Bernal"

print(firstname + '' + lastname)
print(firstname * 3)
print('Dan' in firstname)


# In[57]:


firstname = 'Daniel Hernando Bernal Castaño'.split(' ')[0] #
lastname = "Daniel Hernando Bernal Castaño".split(' ')[-1]
print(firstname)
print(lastname)


# In[58]:


'Daniel' + str(2)


# In[59]:


c = {'Daniel Bernal': "daklus@hotmail.com", 'Hernando Castaño' : 'daklusagency@gmail.com'}


# In[60]:


c["Daniel Bernal"]


# In[61]:


c["Gladys Muñoz"] = None
c["Gladys Muñoz"]


# In[62]:


for name in c:
    print(c[name])


# In[63]:


for email in c.values():
    print(email)    


# In[64]:


for name, email in c.items():
    print(name)
    print(email)


# In[65]:


c


# In[66]:


y


# In[67]:


d = ["Daniel", "Bernal", 'daklus@hotmail.com']
fname, lname, email = d


# In[68]:


fname


# In[69]:


lname


# In[70]:


e = ("Daniel", "Bernal", 'daklus@hotmail.com')
fname, lname, email = e


# In[71]:


fname


# In[72]:


lname


# In[73]:


e = ("Daniel", "Bernal", 'daklus@hotmail.com', 'Zapata')
fname, lname, email = e


# In[74]:


sales_record ={
    'price' : 3.24,
    'num_items' : 4,
    'person' : 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))


# # PYTHON FOR EVERYBODY
# 
# <b>Dr. Charles Servelence<b/>

# In[75]:


x = 1 + 2 * 3 - 8 / 4


# In[76]:


x


# In[77]:


x = int(98.6)
x


# In[78]:


hrs = input("Enter Hours:")
rate = 2.75
pay = float(hrs) * rate

print("pay: ", pay)


# In[79]:


1 + 2.5


# In[80]:


x = 5
if x == 5:
    print("5 is equal")
if x < 6: print('less than 6')
if x != 6:
    print('No equal 6')
    


# ### Loop

# In[81]:


x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print("Is still 5")
    print('Third 5')
print("Afterwards 5")


# In[82]:


for i in range (5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)


# In[83]:


x = 4

if x > 2:
    print("Bigger")
else:
    print('Smaller')
    
print("All done")


# In[84]:


x = 4
if x > 2:
    print("Bigger")
else:
    print('Smaller')
    
print('All done')


# In[85]:


if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')


# In[86]:


x = 15

if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:  # only one is triggered, that's why none of the others apply
    print('Big') # because is indexed in one block
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else:
    print('Ginormous')
    


# In[87]:


x = 1256897
if x < 2: print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')


# In[88]:


x = 6
if x < 2:
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10:  # will never print this because only one stament is execute
    print('Below 10')# and the order influence, first x < 20
else:
    print('Something else')


# ###  Try and Except

# In[89]:


astr = 'Hello Bob'
try:
    istr = int(astr)# in this case there is an error, but we aren't getting a trace back because 
except:  # the code jump the wron code to except
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
    
print('Second', istr)


# In[90]:


astr = 'Hello Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = 1

print('Done', istr)


# In[91]:


rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1
    
if ival > 0:
    print('Nice work')
else:
    print("Not a number")


# In[92]:


x = 2
if  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')


# In[93]:


x = 6

if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')


# In[94]:


astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1


# In[95]:


hrs = input("Enter Hours:")
wage = input("How much do you get per hour: ")
h = float(hrs)
rate = float(wage)
ov = rate * 1.5
reg_h = 40
dif_h = h - reg_h

if h < 40:
    print("Your pay is: ", (reg_h * rate))
elif h > 40:
    print("Your pay is: ", (reg_h * rate) + (dif_h * ov))


# In[96]:


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
#You can use this to cut because the rest of the code does not make sense 

print(fh, fr)

if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr

print("pay: ", xp)


# ## Assignment:
# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# In[97]:


score = input("Enter Score: ")

try:
    sr = float(score)
except:
    print("Error, please enter numeric input")
    quit()

if sr >= 1.0 or sr < 0.0:
    print("Error, please enter numeric in range 0.0 to 1.0")
elif sr >= 0.9:
    print("A")
elif sr >= 0.8:
    print("B")
elif sr >= 0.7:
    print("C")
elif sr >= 0.6:
    print("D")
elif sr < 0.6:
    print("F")


# ## Function

# In[98]:


def thing():
    print("Hello")
    print("Fun")


# In[99]:


thing()
print("Zip")
thing()


# In[100]:


big = max("Hello world")
print(big)


# In[101]:


tiny = min("Hello world")
print(tiny)


# In[102]:


def max(inp):
    blah
    blah
    for x in inp:
        blah
        blah


# In[103]:


print(1 + 2 * float(3) / 4 - 5)


# In[104]:


sval = '123'
ival = int(sval)
print(ival + 1)


# ## Parameters

# In[105]:


def greet(lang):
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
        
greet('fr')
greet('es')
greet('en')


# ## Return Values
# 
# The retunr do two things:
# 1 - Stops the function - jump to that next line
# 2 - Determines the residual value

# In[106]:


def greet():
    return "Hello"

print(greet(), "Glenn")
print(greet(), "Sally")


# In[107]:


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"
    
print(greet ('en'), 'Glenn')
print(greet ('es'), 'Sally')
print(greet ('fr'), 'Michael')
    


# In[108]:


big = max("Hello world")
print(big)

def max(inp):
    for x in inp:
    return 'w'


# ## Multiple Parameters / Arguments

# In[109]:


def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)


# In[110]:


def stuff():
    print('Hello')
    return
    print('World')# jump and never execute

stuff()


# In[111]:


def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)


# In[112]:


def computepay(h, r):
    hrs = input("Enter Hours: ")
    return 

try:
    hr = float(hrs)
except:
    print("Error, please enter numeric input")
    quit()


# In[113]:


def computepay(hrs, rate):
    hrs = input("Enter Hours: ")
    rate = input('Enter rate per hour')
    rgh = 40.0

    try:
        hr = float(hrs)
        rt = float(rate)
    except:
        print("Error, please enter numeric input")
        quit()
    
    #print(hr, rt)
    
    if hr > 40:
        r = (((hr-rgh) * (rt* 1.5)) + (rgh * rt))
        return r
    elif hr <= 40:
        r = (rgh * rate)
        return r  # this r would be the print if we don't need to put return
    
p = computepay(10, 20)
print("Pay", p)

# I have to correct this exercise because if enter numbers is fine but if you enter letters it going to show you an error


# ## Loops and Iteration
# 
# .<b>While</b>
# 
# .<b>break</b>
# 
# .<b>continue</b>

# In[115]:


n = 5
while n > 0:
    print(n)
    n = n - 1 # this is the code that send the iteration to while
print('Blastoff')
print(n)


# In[2]:


n = 0
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off')


# In[116]:


while True: # this is an infinitive loop
    line = input('> ')
    if line == 'done':
        break # this statement ends the current iteration and jumps to the next iteration
    print(line)
print('Done')


# In[6]:


while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')    
# So continue says, oh, we're going to go up to the top. Break says get out and continue says don't do the rest of this iteration but go up and do the next iteration. 


# In[122]:


while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue # quit on the current iteration and go to the next iteration
    if line == 'done':
        break
    print(line)
print('Done')


# ## Definite Loops
#  
# ### for
#  
# The first thing we see in a for loop is we see the iteration variable is explicitly just part of the syntax. i is, you can pick any variable you like. I happen to pick i, and everyone picks i for integer iteration variables. 

# In[10]:


for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')


# ### A define Loop with Strings

# In[12]:


friends = ['Joseph', "Glem", 'Salary']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done')


# Definite loops (for loops) have explicit iteration variables that change each time through a loop.  These iteration variable move through the sequence or set.

# ### Finding the largest value

# In[15]:


largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
    
print('After', largest_so_far)


# We make a variable that contains the largest value we have seen so far. If the current number we are looking at is large, it is the new largest value we have seen so far.

# In[16]:


var_1 = -1
print("Before", var_1)
for numb in [1, 2, 4, 5]:
    if numb > var_1:
        var_1 = numb
    print(var_1, numb)
    
print('After', numb)


# ## Loop Idioms
# 
# ### Counting in a Loop
# 
# To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop.

# In[1]:


zork = 0
print('Before', zork)
for thing in (9, 41, 12, 3, 74, 15):
    zork = zork + 1
    print(zork, thing)
print('After', zork)


# ### Summing in a Loop
# 
# To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop.

# In[2]:


zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print('After', zork)


# ### Finding the Average in a Loop
# 
# An average just combines the counting and sum patterns and divides when the loop is done.

# In[4]:


count = 0
sum = 0
print('Before', count, sum)
for value in  [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)    


# ### Filtering in a Loop
# 
# We use an if statement in the Loop to catch / filter the values we are looking for.

# In[6]:


print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
        print('Large number', value)
print('After')


# ### Search Using a Boolean Variable
# 
# If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.

# In[7]:


found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)


# ### How to find the Smallest Value
# 
# How would we change this to make it find the Smallest value in the list?
# 
# None is a variable, a value, that we can distinctly detect different that numbers.
# 
# We still have a variable that is the smallest so far.  The first time through the loop smallest is None, so we take the first value to be the smallest.

# In[10]:


smallest = None  # Flag value
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)


# <b>The "is" and "is not" Operators</b>
# 
# "Is", "None" and "is not" is also a logical operator.
# You shouldn't use is when you should be using double equals, usually you're using them for a True, False, or None. So that we don't overuse is, because is, is a really, really strong equality. So it's a stronger equality than double equals to, so the double equals is mathematically equal to with potential conversion. 

# # Exercise
# 
# Wirte a program wich repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count and average of the numbers. If the user enters anything other than a number,detect their mistake using "try" and "except" and print an error message and skip to the next number.
# 
# Enter a number: 4
# 
# Enter a number: 5
# 
# Enter a number: bad data
# 
# Invalid input
# 
# Enter a number: 7
# 
# Enter a number: done
# 
# 16 3 5.3333

# In[12]:


num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval
    
print(tot, num, tot/num) # average = total/num


# # Chapter 5
# Graded Quiz

# In[17]:


tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)


# In[18]:


zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)


# In[19]:


smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)


# In[20]:


n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')


# # Assignment 5.2

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# In[1]:


largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        
        n = int(num)
        if largest is None or n > largest:
            largest = n
        elif smallest is None or n < smallest:
            smallest = n
            
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)

print("Minimum is", smallest)


# # Chapter 6

# In[2]:


fruit = 'banana'
letter = fruit[1]
print(letter)


# In[3]:


x = 3
w = fruit[x - 1]
print(w)


# ### Len Function
# 
# A function is some stored code that we use.  A function takes some input and produces an output.

# In[4]:


fruit = 'banana'
x = len(fruit)
print(x)


# ## Looping Through Strings
# 
# Using a while statement and an iteration variable, and the len function, we can construct a loop to look at each of the letters in a string individually.

# In[5]:


fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


# ### A define loop using a for statement is much more elegant
# 
# The iteration variable is completely taken care of by hte for loop

# In[6]:


fruit = 'banana'
for letter in fruit:
    print(letter)


# In[7]:


# is the same output of the code before, and more code, always is better succcinct the code.
index =  0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


# ## Looping and counting
# 
# This is a simple loop that loops through each letter in a string and counts the number of times the loop encounters the 'a' character

# In[8]:


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# ## Slicing Strings
# 
# If we leave off the first number or the last number the slice, it is assumed to be the beginning or end of the string respectively.

# In[9]:


s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])


# ### Using "in" as a Logical Operator
# 
# Then "in" keyword can also be used to check to seee if one string is "in" another string.
# 
# Then "in" expression is a logical True or False and can be used in an if statement.

# In[1]:


fruit = 'banana'
'n' in fruit


# In[2]:


'm' in fruit


# In[3]:


'nan' in fruit


# In[4]:


if 'a' in fruit:
    print('Found it')


# ### Objects are these kinds of variable that have capabilities that are kind of grafted onto or built into them.
# 
# Manipulating Strings

# In[5]:


greet = 'Hello Bob'
zap = greet.lower() # object method
print(zap)


# ## Searching a String
# 
# We use the 'find()' function to search for a substring within another string.
# 
# Find() finds the first occurrence of the substring
# 
# If the substring is not found, find() returns -1
# 
# Remember that string position starts at zero

# In[7]:


fruit = 'banana'
pos = fruit.find('na') # find the substring position within another string 
print(pos)


# In[8]:


aa = fruit.find('z')
print(aa)  # this is like a flag to indicate don't find it


# ### Making Everything UPPER CASE
# 
# You can make a copy of a string in lower case or upper case

# In[10]:


greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)


# ## Search and Replace
# 
# The replace() function is like a "search and replace" operation in a word processor
# 
# It replaces all ocurrences of the search string with the replacement string

# In[9]:


greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)


# ## Stripping Whitespace
# 
# Sometimes we want to take a string and remove whitespace at the beginning and/or end.
# 
# 'Istrip()' and 'rstrip()' remove whitespace at the left or right.
# 
# 'strip()' removes both beginning and ending whitespace

# In[13]:


greet = '       Hello Bob   '
greet.lstrip()


# In[12]:


greet.rstrip()


# In[14]:


greet.strip()


# ### There is a built-in method called "startswith", "line.startswith()".
# 
# Prefixes

# In[16]:


line = 'Please have a nice day'
line.startswith('Please')


# In[17]:


line.startswith('p')


# ## Parsing and Extrating
# 
# From stephen.marquard@uct.ac.za  Sa  Jan  5 09:14:16  2008
# 
# We want to extract this little bit  "uct.ac.za"

# In[18]:


data = 'From stephen.marquard@uct.ac.za Sa Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)


# In[20]:


sppos = data .find(' ', atpos)
print(sppos)


# In[21]:


host = data[atpos+1 : sppos]
print(host)


# ## SUMMARY 
# 
# String TypeError
# 
# Read/convert
# 
# Indexing strings[]
# 
# Slicing strings[2:4]
# 
# Looping through strings with 'for' and 'while'
# 
# Concatenating strings with +
# 
# String operations
# 
# String library
# 
# String Comparisons
# 
# Searching in strings
# 
# Replacing text
# 
# Stripping white space

# # Chapter 6 Quiz
# Graded Quiz • 30 min
# 

# In[22]:


str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)


# In[23]:


x = '40'
y = int(x) + 2
print(y)


# In[24]:


x = 'From marquard@uct.ac.za'
print(x[8])


# In[27]:


x = 'From marquard@uct.ac.za'
print(x[14:17])


# In[28]:


print(len('banana')*7)


# In[29]:


greet = 'Hello Bob'
print(greet.upper())


# In[31]:


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])


# # Assignment 6.5

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

# In[1]:


text = "X-DSPAM-Confidence:    0.8475";
slitext = text.find('0')
ftext = float(text[slitext : ])
print(ftext)


# In[3]:


text = "X-DSPAM-Confidence:    0.8475";  # THis is another option
startPos = text.find(':')
piece = text[startPos+1:]
end = float(piece)
print(end)


# In[ ]:




