#!/usr/bin/env python
# coding: utf-8

# 1. Create an abstract class with abstract and non-abstract methods.
# 2. Create a sub class for an abstract class. Create an object in the child class for the 
# abstract class and access the non-abstract methods
# 3. Create an instance for the child class in child class and call abstract methods
# 4. Create an instance for the child class in child class and call non-abstract method

# In[1]:


#Create an abstract class with abstract and non-abstract methods
# Python program showing
# abstract base class work

from abc import ABC, abstractmethod
class Animal(ABC):

	def move(self):
		pass

class Human(Animal):

	def move(self):
		print("I can walk and run")

class Snake(Animal):

	def move(self):
		print("I can crawl")

class Dog(Animal):

	def move(self):
		print("I can bark")

class Lion(Animal):

	def move(self):
		print("I can roar")
		
# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()


# In[2]:


#Create a sub class for an abstract class. Create an object in the child class for the 
#abstract class and access the non-abstract methods
from abc import ABC, abstractmethod
#Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")
    @abstractmethod
    def interest(self):
        "Abstarct Method"
        pass
#Sub class/ child class of abstract class
class SBI(Bank):
    def balance(self):
        print("Balance is 100")
class Sub1(SBI):
    def interest(self):
        print("In sbi bank interest is 5 rupees")
s= Sub1()
s.bank_info ()
s.balance()
s.interest()


# In[3]:


#Create an instance for the child class in child class and call abstract methods
from abc import ABC, abstractmethod
class One(ABC):
    @abstractmethod
    def calculate(self, a):
        pass
    def m1(self):
        print("implemented method")
class Square(One):
    def calculate(self, a):
        print("square: ", (a*a))
class Cube(One):
    def calculate(self, a):
        print("cube: ", (a*a*a))
s = Square()
c = Cube()
s.calculate(2)
c.calculate(2)


# In[ ]:




