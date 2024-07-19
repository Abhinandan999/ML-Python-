#!/usr/bin/env python
# coding: utf-8

# 
# # Numpy
# 

# ##  1) array

# In[6]:


import numpy as np #Importing numpy.

arr=np.array([1,2,3,4])

print(arr)    #printing array

print(arr[1])#printing array in given index

print(arr[1:3])#Slicing (printing array in syntax arr[start:end])


# ## 2) Simple operations with array using numpy
# 

# In[12]:


import numpy as np #importing numpy
arr=np.array([1,3,5,7,9,2,4,6,8,99])

print(arr+3) #Here each elements adds with 3 

print(arr-1) #Here each elements substarcts with 1

print(arr*6) #Here each elements multiplys  with 6 

print(arr/2) #Here each elements divide with 2 


# # 3) Finding size ,shape,data type

# In[39]:


import numpy as np #Importing numpy.

arr=np.array([1,2,3,4])


print("Printing size of array:- ",np.size(arr))    #printing array size
print("Printing size of single element:- ",np.size(arr[1])) 
print("Printing size of element from index 1 to 4:- ",np.size(arr[1:4])) 



print("Finding shape of array:-",np.shape(arr))

print("Array data type is:- ",arr.dtype)


# # 4)Maths operations
# 

# In[42]:


import numpy as np#importying numpy

arr=np.array([9,8,7,6,5,4,3,2,1])

print("Sum of numbers in given array:- ",np.sum(arr))

print("Mean of numbers in given array:- ",np.mean(arr))

print("Standard deviation of numbers in given array:- ",np.std(arr))


# # 5)Matrix Operations

# In[45]:


import numpy as np

arr=np.array([[1,2],[2,3],[3,4]])
arr1=np.array([[9,8,7],[5,6,4]])

print("Matrix dot product :- ",np.dot(arr,arr1))


# # 6)Randome Module

# In[62]:


import numpy as np

arr=np.array(np.random.rand(5))
print("Random numbers taken by the numpy are:-",arr)

arr1=np.array(np.random.randint(5,9,2))#Here we take numbers using np.random.randint(start,end,number of array)
print("Random Integer numbers taken by the numpy are:-",arr1)


# In[ ]:




