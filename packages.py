#!/usr/bin/env python
# coding: utf-8

# Create a program to create two class.
# 1.1. Create a constructor and a method for each class
# 1.2. Create a __init__.py for adding all packages
# 1.3. Import the respective packages
# 1.4. Call each class by creating an object to it 
# 1.5. Create a program by all the abov

# In[1]:


class Addition:
	first = 0
	second = 0
	answer = 0
	
	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()


# In[ ]:


#

