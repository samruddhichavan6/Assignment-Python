#!/usr/bin/env python
# coding: utf-8

# 1. Different ways creating a string
# 2. Concatenating two strings using + operator
# 3. Finding the length of the string
# 4. Extract a string using Substring
# 5. Searching in strings using index()
# 6. Matching a String Against a Regular Expression With matches()
# 7. Comparing strings
# 8. startsWith(), endsWith() and compareTo()
# 9. Trimming strings with strip()
# 10. Replacing characters in strings with replace()
# 11. Splitting strings with split()
# 12. Converting integer objects to Strings
# 13. Converting to uppercase and lowercase

# In[1]:


#. Different ways creating a string
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


# In[2]:


#Concatenating two strings using + operator
str1="Hello"
str2="World"
print ("String 1:",str1)
print ("String 2:",str2)
str=str1+str2
print("Concatenated two different strings:",str)


# In[3]:


#Finding the length of the string
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
  
str = "Acceptance"
print(findLen(str))


# In[4]:


#Extract a string using Substring
myString = "Mississippi"
print(myString[:]) 
print(myString[4 : ]) 
print(myString[ : 8]) 
print(myString[2 : 7]) 
print(myString[4 : -1]) 
print(myString[-6 : -1]) 


# In[17]:


#Searching in strings using index()
text = 'Python is fun'

# find the index of is
result = text.index('is')
print(result)


# In[21]:


#Matching a String Against a Regular Expression With matches()
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mob = phoneNumRegex.search('My number is 415-555-4242.')
print(mob.group(1))


# In[23]:


#Comparing strings

name = 'John'
name2 = 'john'
name3 = 'doe'
name4 = 'Doe'

print (name == name2)
print (name != name3)
print (name <= name2)
print (name3 >= name2)
print (name4 < name)


# In[24]:


#8. startsWith(), endsWith() and compareTo()
name = "Sam Jose"

print(name.startswith("S"))
print(name.endswith("e"))


# In[26]:


#Trimming strings with strip()
s1 = '  abc  '

print(f'String =\'{s1}\'')

print({s1.lstrip()})

print({s1.rstrip()})

print({s1.strip()})


# In[27]:


#Replacing characters in strings with replace()
a_string = "saaam"
a_string = a_string.replace("a", "b")

print(a_string)


# In[29]:


#Splitting strings with split()
txt = "welcome to the show"

x = txt.split()

print(x)


# In[38]:


#Converting integer objects to Strings
num = 99
str(num)


# In[39]:


#Converting to uppercase and lowercase
string = 'MANGO'
print(string.lower()) 
string = 'mango'
print(string.upper())


# In[ ]:




