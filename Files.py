#!/usr/bin/env python
# coding: utf-8

# 1. Write a program to read text file
# 2. Write a program to write text to .txt file using InputStream
# 3. Write a program to read a file stream
# 4. Write a program to read a file stream supports random access
# 5. Write a program to read a file a just to a particular index using seek()
# 6. Write a program to check whether a file is having read access and write access permission

# In[4]:


file = open('sample.txt', 'w')
file.write("I am a Python programmer.\nI am happy.")
file.close()


# In[5]:


#Write a program to read text file
file = open('sample.txt', 'r')
data = file.read()
# printing the data
print(data)
# closing the file
file.close()


# In[2]:


#Write a program to read a file a just to a particular index using seek()
f = open("sample.txt", "r")
f.seek(6)
print(f.readline())


# In[6]:


#. Write a program to check whether a file is having read access and write access permission
import os
print(os.access('sample.txt', os.R_OK)) # Check for read access
print(os.access('sample.txt', os.W_OK)) # Check for write access
print(os.access('sample.txt', os.X_OK)) # Check for execution access
print(os.access('sample.txt', os.F_OK)) # Check for existance of file


# In[ ]:




