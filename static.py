#!/usr/bin/env python
# coding: utf-8

# 1. Define a static variable and access that through a class 
# 2. Define a static variable and access that through a instance
# 3. Define a static variable and change within the instance
# 4. Define a static variable and change within the class

# # Define a static variable and access that through a class 
# When we declare a variable inside a class but outside any method, it is called as class or static variable in python. 
# Class or static variable can be referred through a class but not directly through an instance

# In[6]:


#Define a static variable and access that through a instance
class example:
    
    staticVariable = 9 # Access through class

print (example.staticVariable) 

#Access through an instance
instance = example()
print(instance.staticVariable) 


# In[8]:


#Define a static variable and change within the instance
class example:
     staticVariable = 9 

print (example.staticVariable) 


#Change within an instance
instance.staticVariable = 12
print(instance.staticVariable) 
print(example.staticVariable)


# In[18]:


# Define a static variable and change within the class


# In[ ]:




