#!/usr/bin/env python
# coding: utf-8

# 1. Write two methods with the same name but different number of parameters of same type 
# and call the methods 
# 2. Write two methods with the same name but different number of parameters of different 
# data type and call the methods 
# 3. Write two methods with the same name and same number of parameters of same type

# In[10]:


#Write two methods with the same name but different number of parameters of same type 
#and call the methods

def product(a, b):
	p = a * b
	print(p)
	

def product(a, b, c):
	p = a * b*c
	print(p)

product(4, 5, 5)


# In[12]:


#Write two methods with the same name but different number of parameters of different 
#data type and call the methods 

def add(datatype, *args):
	if datatype =='int':
		answer = 0
		

	if datatype =='str':
		answer =''

	for x in args:


		answer = answer + x

	print(answer)

# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Jonny')


# In[ ]:




