#!/usr/bin/env python
# coding: utf-8

# 1. Write a function to add integer values of an array
# 2. Write a function to calculate the average value of an array of integers
# 3. Write a program to find the index of an array element
# 4. Write a function to test if array contains a specific value
# 5. Write a function to remove a specific element from an array
# 6. Write a function to copy an array to another array
# 7. Write a function to insert an element at a specific position in the array
# 8. Write a function to find the minimum and maximum value of an array
# 9. Write a function to reverse an array of integer values
# 10. Write a function to find the duplicate values of an array
# 11. Write a program to find the common values between two arrays
# 12. Write a method to remove duplicate elements from an array
# 13. Write a method to find the second largest number in an array
# 14. Write a method to find the second largest number in an array
# 15. Write a method to find number of even number and odd numbers in an array
# 16. Write a function to get the difference of largest and smallest value
# 17. Write a method to verify if the array contains two specified elements(12,23)
# 18. Write a program to remove the duplicate elements and return the new arra

# In[1]:


arr = [1, 2, 3, 4, 5];     
sum = 0;    
        
for i in range(0, len(arr)):    
   sum = sum + arr[i];    
     
print("Sum of all the elements of an array: " + str(sum)); 


# In[2]:


def average( a , n ):
 
    sum = 0
    for i in range(n):
        sum += a[i]
     
    return sum/n;
 
arr = [10, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print(average(arr, n))


# In[3]:




arr1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]


print(arr1.index(4))



# In[5]:


numbers =[1,6,9,5,3]
for num in numbers:
    if num == 3:
        print('Exist')


# In[10]:


#Write a function to remove a specific element from an array
array=[10,20,30,40,50,60,70,80,90]
print(array.pop(8))
print(array)


# In[14]:


#Write a function to copy an array to another array
arr1 = [1, 2, 3, 4, 5];     
   
arr2 = [None] * len(arr1);    
       
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i];     
     
    
print("Elements of original array: ");    
for i in range(0, len(arr1)):    
    print(arr1[i]),    
     
print();    
     
    
print("Elements of new array: ");    
for i in range(0, len(arr2)):    
    print(arr2[i]),  


# In[15]:


#Write a function to insert an element at a specific position in the array
arr1=[6,9,0,4,6]
arr1.insert(5,10)
print(arr1)


# In[17]:


#Write a function to find the minimum and maximum value of an array
Array= [67,89,90,45,6,32]
print(max(Array))
print(min(Array))


# In[18]:


#Write a function to reverse an array of integer values
def reverseArray(A,start,end):
    while start < end:
        A[start],A[end]= A[end],A[start]
        start += 1
        end -= 1
A = [1,2,3,4,5]
print(A)
reverseArray(A,0,4)
print('reverse list is : ')
print(A)


# In[19]:


#10. Write a function to find the duplicate values of an array
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];     
     
print("Duplicate elements in given array: ");        
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j]);    


# In[20]:


#. Write a program to find the common values between two arrays
a=[1,2,3,4] 
b=[4,5,6,7] 
print([s for s in a if s in b]) 


# In[21]:


#Write a method to remove duplicate elements from an array
a = [2, 3, 3, 2, 5, 4, 4, 6]
 
b = []
 
for i in a:
    
    if i not in b:
        b.append(i)
 
print(b)


# In[30]:


#Write a method to find the second largest number in an array
list1 = [10, 20, 4, 45, 99]
 
list1.sort()

print("Second largest element is:", list1[-2])


# In[31]:


#Write a method to find number of even number and odd numbers in an array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
            count_even+=1
        else:
             count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


# In[32]:


# Write a function to get the difference of largest and smallest value
def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]
     
    for i in range( 0, arr_size ):
        for j in range( i+1, arr_size ):
            if(arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]
     
    return max_diff
     
arr = [1, 2, 90, 10, 110]
size = len(arr)
print ("Maximum difference is", maxDiff(arr, size))


# In[35]:


#Write a program to remove the duplicate elements and return the new arra
def removeDuplicates(arr, n):
 

    if n == 0 or n == 1:
        return n
 
    temp = list(range(n))
 
    j = 0;
    for i in range(0, n-1):
 
        
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1
 
    
    temp[j] = arr[n-1]
    j += 1
     

    for i in range(0, j):
        arr[i] = temp[i]
 
    return j
 
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
n = len(arr)
 
n = removeDuplicates(arr, n)

for i in range(n):
    print ("%d"%(arr[i]), end = " ")


# In[ ]:




