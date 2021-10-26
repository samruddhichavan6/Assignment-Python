#!/usr/bin/env python
# coding: utf-8
. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
1.1. Adding the values in dictionary
1.2. Updating the values in dictionary
1.3. Accessing the value in dictionary
1.4. Create a nested loop dictionary
1.5. Access the values of nested loop dictionary
1.6. Print the keys present in a particular dictionary
1.7. Delete a value from a dictionary
# In[6]:


#Create a Dictionary with at least 5 key value pairs of the Student ID and Name
Id={"Laxman":5656, "Simran":6587, "Amit":5177, "Julie":6898, "Kavita":4566}
Id


# In[9]:


Id['Smita']=8907
Id


# In[14]:


#Updating the values in dictionary
Id={"Laxman":5656, "Simran":6587, "Amit":5177, "Julie":6898, "Kavita":4566}
updated_Id = {'Rashi':4808}

Id.update(updated_Id)


print(Id)


# In[19]:


# Accessing the value in dictionary
print ("Dict key-value of Id : ")
for i in Id:
    print(i, Id[i])


# In[26]:


#Create a nested loop dictionary
Id = {'std1': {'name': 'Laxman', 'id': '5656'},
     'std2': {'name': 'Simran', 'id': '6587'},
     'std3': {'name': 'Amit', 'id': '5177'},
     'std4': {'name':'Julie','id':'6898'},
     'std5': {'name':'Kavita','id':'4566'}}


print(Id)


# In[28]:


#Access the values of nested loop dictionary
Id = {'std1': {'name': 'Laxman', 'id': '5656'},
     'std2': {'name': 'Simran', 'id': '6587'},
     'std3': {'name': 'Amit', 'id': '5177'},
     'std4': {'name':'Julie','id':'6898'},
     'std5': {'name':'Kavita','id':'4566'}}
print(Id['std1']['id'])


# In[29]:


#Print the keys present in a particular dictionary
Id = {'std1': {'name': 'Laxman', 'id': '5656'},
     'std2': {'name': 'Simran', 'id': '6587'},
     'std3': {'name': 'Amit', 'id': '5177'},
     'std4': {'name':'Julie','id':'6898'},
     'std5': {'name':'Kavita','id':'4566'}}
print(Id['std1']['name'])


# In[34]:


#Delete a value from a dictionary
Id = {'std1': {'name': 'Laxman', 'id': '5656'},
     'std2': {'name': 'Simran', 'id': '6587'},
     'std3': {'name': 'Amit', 'id': '5177'},
     'std4': {'name':'Julie','id':'6898'},
     'std5': {'name':'Kavita','id':'4566'}}
del Id['std1']['name']


# In[ ]:




