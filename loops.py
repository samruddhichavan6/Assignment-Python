#!/usr/bin/env python
# coding: utf-8

# 1. Write a program to print “Bright IT Career” ten times using for loop
# 2. Write a java program to print 1 to 20 numbers using the while loop.
# 3. Program to equal operator and not equal operators
# 4. Write a program to print the odd and even numbers.
# 5. Write a program to print largest number among three numbers.
# 6. Write a program to print even number between 10 and 20 using while
# 7. Write a program to print 1 to 10 using the do-while loop statement.
# 8. Write a program to find Armstrong number or not
# 9. Write a program to find the prime or not.
# 10. Write a program to palindrome or not.
# 11. Program to check whether a number is EVEN or ODD using switch
# 12. Print gender (Male/Female) program according to given M/F using switch

# In[4]:


for i in range(10):
    print("Bright IT Career")


# In[6]:


i=1
while(i<+20):
    i+=1
    print(i)
    


# In[8]:


a=10
b=10
if(a==b):
    print (True)
else :
    print (False)


# In[9]:


a=6
b=9
if(a!=b):
    print(True)
else:
    print(False)


# In[10]:


num = int(input("enter the number"))
if(num%2==0):
    print('even')
else:
    print('odd')
    


# In[11]:


num1 = 10
num2 = 14
num3 = 12


if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


# In[12]:


x = int(input("Enter a number:"))
i = 1
while i <= x:
    if i % 2 == 0:
        print("Number is even:", i)
    i = i + 1


# In[15]:


count = 1

while True:
    print(count)

    count += 1
    

    if count>10:
        break
        


# In[18]:


num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
     print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# In[19]:


num=int(input("enter the number"))
if(num%2==0):
    print('Not Prime')
else:
    print('Prime')


# In[20]:


num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


# In[23]:


def gender():
        switcher={
                0:'Female',
                1:'Male',
             }
        return switcher.get(i,"Invalid ")


# In[ ]:




