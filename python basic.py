#!/usr/bin/env python
# coding: utf-8

#  1. Write a program to print your name.
# 2. Write a program for a Single line comment and multi-line comments
# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the 
#    Console.
# 4. Define the local and Global variables with the same name and print both variables and 
#    understand the scope of the variable

# In[2]:


print('Samruddhi')


# In[3]:


#single line command


# In[4]:


#multi line command
#expands more line here.


# In[5]:


a=5
print(type(a))


# In[6]:


b=5.6
print(type(b))


# In[7]:


c=2+6j
print(type(c))


# In[8]:


print(type(True))
print(type(False))


# In[9]:


a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

print('global : ', a)
f()
print('global : ', a)
g()


# In[ ]:




