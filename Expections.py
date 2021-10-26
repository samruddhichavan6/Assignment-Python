#!/usr/bin/env python
# coding: utf-8
Write a program to generate Arithmetic Exception without exception handling
2. Handle the Arithmetic exception using try-catch block
3. Write a method which throws exception, Call that method in main class without try block
4. Write a program with multiple catch blocks
5. Write a program to throw exception with your own message
6. Write a program to create your own exception
7. Write a program with finally block
8. Write a program to generate Arithmetic Exception
9. Write a program to generate FileNotFoundException
10. Write a program to generate ClassNotFoundException
11. Write a program to generate IOException
12. Write a program to generate NoSuchFieldException
# In[1]:


#Write a program to generate Arithmetic Exception without exception handling
# initialize the amount variable
marks = 10000

# perform division with 0
a = marks / 0
print(a)


# In[2]:


#Write a method which throws exception, Call that method in main class without try block
try:
    a=5
    b='0'
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")


# In[3]:


#Write a program with multiple catch blocks
import math


def square(x):
    if int(x) is 0:
        raise ValueError('Input argument cannot be zero')
    if int(x) < 0:
        raise TypeError('Input argument must be positive integer')
    return math.pow(int(x), 2)
    else :
        return 0
while True:

    try:
        y = square(input('Please enter a number\n'))
        print(y)
    except ValueError as ve:
        print(type(ve), '::', ve)
    except TypeError as te:
        print(type(te), '::', te)


# In[4]:


#Write a program to throw exception with your own message
 while True:
    try:
         x = int(input("Please enter a number: "))
            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# In[5]:


#Write a program to create your own exception

try:
  1/0
 
except Exception as err:
  # perform any action on Exception instance
  print("Error:", err)


# In[6]:


#Write a program to generate Arithmetic Exception
try:
	a = 10/0
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")
else:
	print ("Success.")


# In[7]:


#Write a program to generate FileNotFoundException
import sys
# open mytext.txt file in read mode

try:
    file1 = open("d:/mytext2.txt", "r")

except FileNotFoundError:
        print("Sorry file not found")
        sys.exit()
# Read all contents of text file in a string s

s = file1.read()

# show the contents from string s

print(s)

# close the text file
file1.close()


# In[9]:


#Write a program to generate ClassNotFoundException

public class Example :
	
	 public static void main(String args[]) 
		try
		
		Class.forName("Dogs")
		
	    catch (ClassNotFoundException ex)
		
			ex.printStackTrace()


# In[10]:


#Write a program to generate IOException

file = open('My_file')
lines = file.readline()
slines = int(lines.strip())


# In[ ]:





# In[ ]:




