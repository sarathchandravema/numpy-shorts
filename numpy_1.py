#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = [1,2,3,4,5]
b = [i**2 for i in a]
print(b)


# In[3]:


a = np.array([1,2,3,4,5])
a**2


# In[4]:


b = np.array([1,2,3,4,5])
b


# In[5]:


print(b)


# In[6]:


type(b)


# In[7]:


b.dtype


# In[8]:


a = range(10000)


# In[9]:


get_ipython().run_line_magic('timeit', '[i**2 for i in a]')


# In[10]:


b = np.arange(10000)


# In[11]:


get_ipython().run_line_magic('timeit', 'b**2')


# In[ ]:





# In[12]:


a = range(10)


# In[13]:


print(a)


# In[14]:


for i in a:
    print(i, end="  ")


# In[15]:


b = np.arange(0, 10)
print(b)


# In[16]:


a = range(1,10,2)
for i in a:
    print(i, end= " ")


# In[17]:


b = np.arange(1, 10, 2)
print(b)


# Below one throws error, as python range doesnt support float step size

# In[18]:


a = range(1,10,2.4)
for i in a:
    print(i, end= " ")


# In[19]:


b = np.arange(1, 10, 0.5)
print(b)


# In[20]:


b = np.array([1,2,3,4,5])
print(type(b))
print(b.dtype)
print(b)


# In[21]:


b = np.array([1,2,3,4,5, 4.5])
print(type(b))
print(b.dtype)
print(b)


# In[22]:


b = np.array([1,2,3,4,5, "e"])
print(type(b))
print(b.dtype)
print(b)


# In[23]:


b = np.array([1,2,3,4,5, True])
print(type(b))
print(b.dtype)
print(b)


# In[24]:


b = np.array([1,2,3,4,5,"er", True])
print(type(b))
print(b.dtype)
print(b)


# What is object datatype ?? and what happens if one of the element is object datatype

# In[25]:


b = np.array([1,2,3,4,5])
print(b.ndim)
print(b.shape)


# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


get_ipython().run_line_magic('pinfo', 'np.linspace')


# In[27]:


help(np.linspace)


# In[28]:


a = np.linspace(1, 10, 10)
print(a)


# In[29]:


a = np.linspace(1, 10, 20)
print(a)


# The above values are equally spaced values

# In[30]:


a = np.linspace(1, 10, 19)
print(a)


# In[101]:


type(np.linspace(1,10, 19))


# In[ ]:





# 2D arrays

# In[31]:


a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a


# In[32]:


print(a)


# In[33]:


a.ndim


# In[34]:


a.shape


# In[ ]:





# In[35]:


b = np.array([[1,2,3],[4,5,6,7],[7,8,9]])
b


# In[36]:


b.ndim


# In[ ]:





# In[37]:


a=np.arange(1,13)
a


# In[38]:


a.reshape(1,12)


# In[39]:


a.reshape(2,6)


# In[40]:


a.reshape(3,4)


# In[41]:


a.reshape(6,2)


# In[42]:


a.reshape(12, 1)


# In[43]:


a.reshape(-1,6)


# Bothe the dimensions,rows and columns cannt be unknown

# In[44]:


a.reshape(-1,-1)


# In[45]:


a.reshape(10,2)


# In[ ]:





# In[47]:


b = np.arange(1,17)
b


# In[48]:


b.reshape(2,8)


# In[ ]:





# In[52]:


b = np.arange(1,13)
b


# In[53]:


c = b.reshape((3,4))
print(c)


# In[54]:


print(b.reshape(4,3))


# In[55]:


print(c.T)


# From above, reshape is different from Transpose. Evident that output of reshape from (3,4) to (4,3) is different from output of Transpose of (3,4).

# In[ ]:





# In[ ]:





# Flatten converts everything to 1D matrix

# In[57]:


c.flatten()


# In[ ]:





# In[ ]:





# In[59]:


a = np.arange(1,13).reshape((3,4)) # this is chaining
print(a)


# In[ ]:





# In[ ]:





# Slicing

# In[60]:


a = np.arange(1,13)
print(a)


# In[61]:


a[0:5]


# In[62]:


a[5:-1]


# In[63]:


a[5:10]


# In[64]:


a[-1]


# In[65]:


a[4]


# In[66]:


a[-4:]


# In[67]:


a[-4:-1]


# In[69]:


a[-4:0] # this is interesting


# We can jump values also while slicing, as below

# In[70]:


a[::3] #[start:end:step]


# In[71]:


a[::-1]


# In[72]:


a[::-2]


# In[74]:


a[1:8:-2]


# In[75]:


a[8:1:-2]


# In[73]:


a[-2:-10:-2] #his will work until our start value is greater than stop value


# In[ ]:





# 2D slicing

# In[85]:


a = np.arange(1,13).reshape((4,3))
print(a)


# In[86]:


# a[row][column] -> method1 and not suggested
# a[row, column] -> method2


# In[87]:


a[0]


# In[88]:


a[0,:]


# In[89]:


a[:2, :]


# In[90]:


a[:2]


# In[91]:


a[1:3, :]


# In[92]:


a[1:3, :2]


# In[93]:


a[::2, ::2]


# In[94]:


a[1::2, ::2]


# For specific rown and columns, we can provide tuple.
# Either rows or columns to be specific. Both specific will refer to points

# In[97]:


a[[0,1,3], :]


# In[100]:


a[:,[0,2,1]]


# In[99]:


a[[0,1,3], [1,2,0]]


# In[ ]:




