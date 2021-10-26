#!/usr/bin/env python
# coding: utf-8
Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method.
Create a sub class and try to access the private fields and methods from sub class.
2. Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package. 
Also, Access the PROTECTED fields and methods from child class located in a different 
package
Access the PROTECTED fields and methods from any class in different package
3. Create a class with PUBLIC fields and methods. 
Access the public methods and fields from any class in the same package or different 
package
# In[2]:


#Create a class with PRIVATE fields, private method and a main method. Print the fields 
#in main method. Call the private method in main method.

class A: 
    
    # Declaring public method
    def fun(self):
        print("Public method")
    
    # Declaring private method
    def __fun(self):
        print("Private method")
          
# Driver's code
obj = A()
  
# Calling the private member 
# through name mangling
obj._A__fun()


# In[3]:


class Super:
     
     # public data member
     var1 = None
 
     # protected data member
     _var2 = None
      
     # private data member
     __var3 = None
     
     # constructor
     def __init__(self, var1, var2, var3): 
          self.var1 = var1
          self._var2 = var2
          self.__var3 = var3
     
    # public member function  
     def displayPublicMembers(self):
  
          # accessing public data members
          print("Public Data Member: ", self.var1)
        
     # protected member function  
     def _displayProtectedMembers(self):
  
          # accessing protected data members
          print("Protected Data Member: ", self._var2)
      
     # private member function  
     def __displayPrivateMembers(self):
  
          # accessing private data members
          print("Private Data Member: ", self.__var3)
 
     # public member function
     def accessPrivateMembers(self):    
           
          # accessing private member function
          self.__displayPrivateMembers()
  
# derived class
class Sub(Super):
  
      # constructor
       def __init__(self, var1, var2, var3):
                Super.__init__(self, var1, var2, var3)
           
      # public member function
       def accessProtectedMembers(self):
                 
                # accessing protected member functions of super class
                self._displayProtectedMembers()
  
#creating objects of the derived class    
obj = Sub("Geeks", 4, "Geeks !")
 
# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
 
# Object can access protected member
print("Object is accessing protected member:", obj._var2)
 
# object can not access private member, so it will generate Attribute error
#print(obj.__var3)


# In[ ]:




