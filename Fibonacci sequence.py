#!/usr/bin/env python
# coding: utf-8

# In[1]:


# to print the first n numbers of the fibonacci sequence


# In[2]:


# create a list of the first twenty thousand numbers of the fibonacci sequence 


# In[3]:


fsequence = [0, 1]


# In[4]:


while len(fsequence) < 20000:
    x = fsequence[-1] + fsequence[-2]
    fsequence.append(x)


# In[5]:


# function to print the first n numbers of the fibonacci sequence 


# In[6]:


def fibonacci(x):
    if type(x) == int:
        if x >= 0 and x <= 20000 :
            print(fsequence[0:x])
        else:
            print('Input a positive integer less than twenty thousand (20000)')
    else:
        print('Input a positive integer')

fibonacci(300)
