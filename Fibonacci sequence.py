#!/usr/bin/env python
# coding: utf-8

# In[1]:


# to print the first n numbers of the fibonacci sequence


# In[2]:


# create a list of the first nineteen thousand numbers of the fibonacci sequence 


# In[3]:


fsequence = [0, 1]


# In[4]:


while fsequence[-1] <= 100 ** 2000:
    x = fsequence[-1] + fsequence[-2]
    fsequence.append(x)


# In[5]:


# function to print the first n numbers of the fibonacci sequence 


# In[6]:


def fibonacci(x):
    if type(x) == int:
        if x >= 0 and x <= 19143 :
            print(fsequence[0:x])
        else:
            print('Input a positive integer less than 19143')
    else:
        print('Input a positive integer')


# In[7]:


fibonacci(200000)


# In[8]:


fibonacci('two')


# In[9]:


fibonacci(0)


# In[10]:


fibonacci(1.0)


# In[11]:


fibonacci(-34)

