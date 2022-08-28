#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Welcome to Numpy-4')


# In[2]:


import numpy as np


# In[3]:


import math
a = np.arange(1,11)
func = np.vectorize(math.log)
func(a)


# In[4]:


def cube(s):
    return s**3


# In[5]:


func1=np.vectorize(cube)
func1(a)


# In[6]:


def complicated(s):
    return np.exp(s-1)
func2 = np.vectorize(complicated)
func2(a)


# In[7]:


func1(func(a))


# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


a = np.arange(4)
a


# In[9]:


b = a.reshape(2,2)
b


# In[10]:


a[0]=100


# In[11]:


print(a)
print(b)


# In[12]:


b[0,1] = 22


# In[13]:


print(b)
print(a)


# In[ ]:





# In[14]:


c=a+1
c


# In[15]:


c[2]=99


# In[16]:


a


# In[ ]:





# In[ ]:





# In[17]:


a = np.arange(4)
a


# In[18]:


d = a*1
d


# In[19]:


d[0] = 100
d


# In[20]:


a


# In[21]:


b=a+0
b


# In[22]:


b[1]=100
b


# In[23]:


a


# In[24]:


np.shares_memory(a,b)


# In[ ]:





# In[25]:


a = np.arange(4)
b = a.reshape((2,2))
print(a)
print(b)


# In[26]:


np.shares_memory(a,b)


# In[27]:


a[2]=111
print(a)
print(b)


# In[ ]:





# In[28]:


a=np.arange(1,13).reshape((3,4))
b=a.reshape((6,2))
print(a)
print(b)


# In[29]:


print(a.shape)


# In[30]:


print(b.shape)


# In[31]:


print(a.ndim)
print(b.ndim)


# In[32]:


np.shares_memory(a,b)


# In[33]:


b[1,1]=99
b


# In[34]:


a


# In[35]:


c=b*2


# In[36]:


a


# In[37]:


b


# In[38]:


c


# In[39]:


d=b.reshape((4,3))


# In[40]:


np.shares_memory(d,a)


# In[ ]:





# In[ ]:





# In[41]:


a = np.arange(10)
a


# In[42]:


b=a


# In[43]:


b


# In[44]:


c = a.copy()


# In[45]:


c


# In[46]:


c[0]=100
c


# In[47]:


a


# In[48]:


a[2]=123


# In[49]:


a


# In[50]:


c


# In[51]:


b


# In[52]:


np.shares_memory(a, b)


# In[53]:


np.shares_memory(c,a)


# In[ ]:





# In[ ]:





# In[54]:


a=np.arange(10)
a


# In[55]:


b=a
b


# In[56]:


id(a)


# In[57]:


id(b)


# In[58]:


c=a.reshape(2,-1)


# In[59]:


id(c)


# In[60]:


d=a.view() ##shallow copy


# In[61]:


a


# In[62]:


a[3]=123


# In[63]:


a


# In[64]:


d


# In[65]:


b


# In[66]:


c


# In[ ]:





# In[ ]:





# In[67]:


a = np.arange(1,25).reshape((2,3,4))
a


# In[68]:


np.sum(a, axis=0) #in depth direction


# In[69]:


np.sum(a, axis=1) # in vertical direction


# In[70]:


np.sum(a, axis=2) # in horizontal direction


# In[71]:


a.T


# In[ ]:





# In[ ]:





# In[72]:


a[0,:,:]


# In[73]:


a[:,:,0]


# In[74]:


a[:,:,::2]


# In[ ]:





# In[75]:


# splitting


# In[78]:


d = np.arange(1,13)
d


# In[79]:


np.split(d,3)


# In[80]:


np.split(d,2)


# In[81]:


np.split(d,6)


# In[82]:


np.split(d,12)


# In[84]:


np.split(d, [3,5,7])


# In[85]:


np.split(d, [3,5,7,14])


# In[86]:


np.split(d, [3,5,7,14,18])


# In[87]:


np.split(d, [3,5,7,11,14,18])


# In[88]:


np.split(d, [3,3,5,7,11,14,18])


# In[89]:


np.split(d, [12, 7, 4,0])


# In[ ]:





# In[90]:


d = np.arange(1,13).reshape((3,4))
d


# In[91]:


np.split(d, 2 ,axis=1)


# In[92]:


np.split(d, 4 ,axis=1)


# In[93]:


np.split(d, 3 ,axis=0)


# In[94]:


np.split(d, [1,2] ,axis=1)


# In[95]:


np.split(d, [1] ,axis=0)


# In[ ]:





# In[ ]:





# In[96]:


a = np.arange(9).reshape((3,3,1))
a


# In[103]:


#np.squeeze?


# In[98]:


x = np.array([[[0], [1], [2]]])


# In[99]:


x.shape


# In[100]:


np.squeeze(x)


# In[101]:


np.squeeze(a)


# In[102]:


np.squeeze(a).shape


# In[104]:


np.squeeze(x, axis=0)


# In[106]:


#np.squeeze(x, axis=1)


# In[ ]:





# In[109]:


b = np.arange(9).reshape((3,3))
b


# In[110]:


np.expand_dims(b,axis=2)


# In[111]:


get_ipython().run_line_magic('pinfo', 'np.expand_dims')


# In[117]:


x = np.array([5, 9])


# In[118]:


y = np.expand_dims(x, axis=0)
y


# In[119]:


b=np.arange(9).reshape((3,3))
b


# In[120]:


np.expand_dims(b, axis=2)


# In[ ]:




