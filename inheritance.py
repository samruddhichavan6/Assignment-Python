#!/usr/bin/env python
# coding: utf-8
A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B. 
Create three methods in each class, 2 methods are specific to each class and third 
method (override method) should be in all three Classes A, B and C
Create a class with main method. Create an object for each class A, B and C in main 
method and call every method of each class using its own object/instance.
Call an overridden method with super class reference to B and C class’s objects
Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
process only for data member
# In[1]:


class A(): 
        
    
    def display(self):
        print("Inside A")
    
    
class B(A): 
    
    def show(self):
        print("Inside B")
    

class C(B): 
          
    # Child's show method
    def show(self):
        print("Inside C")         
    
# Driver code 
g = C()   
g.show()
g.display()


# In[3]:


#Create a class with main method. Create an object for each class A, B and C in main 
#method and call every method of each class using its own object/instance.

class Parent:        # define parent class
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print ('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
    def __init__(self):
        print ("Calling child constructor")

    def childMethod(self):
        print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


# In[5]:


#Call an overridden method with super class reference to B and C class’s objects
class Parent(object):
    def A(self):
        print ("in A")
class Child(Parent):
    def A(self):
       print ("in B")

C=Child()


# In[6]:


#Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
#process only for data member
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# In[ ]:




