#!/usr/bin/env python
# coding: utf-8
Write a class with a default constructor, one argument constructor and two argument 
constructors. Instantiate the class to call all the constructors of that class from a main 
class
2. Call the constructors(both default and argument constructors) of super class from a child 
class
3. Apply private, public, protected and default access modifiers to the constructor
4. Write a program which illustrates the concept of attributes of a constructor
# In[1]:


#Write a class with a default constructor, one argument constructor and two argument 
#constructors. Instantiate the class to call all the constructors of that class from a main 
#class

class Animals:

# default constructor
def __init__(self):
    self.geek = "Dog"

# a method for printing data members
def print_Geek(self):
        print(self.geek)


# creating object of the class
obj = Animals()

# calling the instance method using the object obj
obj.print_Geek()


# In[6]:


#Call the constructors(both default and argument constructors) of super class from a child 
#class

class Class():
    def __init__(self, x):
        print(x)
class SubClass(Class):
    def __init__(self, x):
  
    
        super().__init__(x)
x = [1, 2, 3, 4, 5]
a = SubClass(x)


# In[7]:


#Apply private, public, protected and default access modifiers to the constructor
# program to illustrate access modifiers of a class

# super class
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

# creating objects of the derived class	
obj = Sub("Dogs", 4, "Cats!")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)


# In[10]:


#Write a program which illustrates the concept of attributes of a constructor

class Individual:
    def __init__(self):
        self.Student_Name = input( " Enter Name of the student : " )
        self.Student_age = input( " Enter age of the student : " )
        self.Student_gender = input( " Enter gender of the student : " )

    def display(self):
        print( " \n \n Enter Name of the student : " , self.Student_Name )
        print( " Enter age of the student : " , self.Student_age )
        print( " Enter gender of the student : " , self.Student_gender )

class Evaluated_Marks:

    def __init__(self):
        self.stuClass = input( " Class of the student : " )
        print( " Evaluated Marks per subject : " )
        self.literature = int(input( " Mark in Literature subject : " ))
        self.math = int(input( " Mark in Math subject : " ))
        self.biology = int(input( " Mark in Biology subject : " ))
        self.physics = int(input( " Mark in Physics subject : " ))

    def display(self):
        print( " Study in : " ,self.stuClass)
        print( " Total Evaluated_Marks : " , self.literature + self.math + self.biology + self.physics)
class student(Individual, Evaluated_Marks):
    def __init__(self):
        Individual.__init__(self)

        Evaluated_Marks.__init__(self)
    def result(self):

        Individual.display(self)
# Call method of class 'Evaluated_Marks'
        Evaluated_Marks.display(self)
#      Objects of class 'student'    #
        Student1 = student()
        Student2 = student()
        print("                                                                           ")
        print( " Note : The instances get initialized with the given values Successfully " )


# In[ ]:




