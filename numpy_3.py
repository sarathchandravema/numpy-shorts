#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome Numpy-3")


# In[2]:


import numpy as np


# In[3]:


a = np.array([4,2,65,56,0,6,9])
a


# In[4]:


np.sort(a)


# In[5]:


a


# In[6]:


a.sort() # this is ndarray.sort


# In[7]:


a


# Difference b/n ndarray.sort() and np.sort(ndarray) is that inplace and permanent sorting for earlier while the latter just sorts and returns but doesn't store.
# 
# Above is the example.

# In[8]:


a = np.array([4,2,65,56,0,6,9])


# In[9]:


np.argsort(a)


# In[10]:


np.max(a)


# In[11]:


np.argmax(a)


# In[12]:


a = np.array([4,2,65,56,0,65, 6,9]) #multiple max values


# In[13]:


np.max(a)


# In[14]:


np.argmax(a)


# In[15]:


np.sort(a)


# In[16]:


np.argsort(a)


# In[ ]:





# In[17]:


b = np.array([[23,2,54], [17,3,42], [15,5,65]])
b


# In[18]:


np.sum(b)


# In[19]:


np.sort(b) # defaults to last axis or max axis, in 2-d it is axis=1


# In[20]:


np.sort(b, axis=0)


# In[21]:


np.argsort(b)


# In[22]:


np.argsort(b, axis=1)


# In[23]:


np.argsort(b, axis=0)


# In[24]:


get_ipython().run_line_magic('pinfo', 'np.sort')


# In[31]:


### This is unpacking
a,b,c = [1,2,3]


# In[32]:


print(a)
print(b)
print(c)


# In[41]:


data1=np.array([1, 2, 3])
print(data1)


# In[42]:


data1.shape


# In[43]:


a,b,c = data1.T


# In[44]:


print(a)
print(b)
print(c)


# In[25]:


data=np.loadtxt('fitness.txt', dtype='str')


# In[27]:


data[:5]


# In[28]:


data.shape


# In[29]:


data[0]


# In[30]:


data.T


# In[38]:


date,step_count,mood,calories_burned, hours_of_sleep,bool_of_active,weight_kg = data.T


# In[39]:


step_count


# In[45]:


step_count=np.array(step_count, dtype='int')


# In[64]:


hours_of_sleep = np.array(hours_of_sleep, dtype='int')


# In[46]:


step_count


# In[47]:


np.mean(step_count)


# In[48]:


mood


# In[49]:


mood[mood=='100'] = 'sad'
mood[mood=='200'] = 'neutral'
mood[mood=='300'] = 'happy'


# In[50]:


mood


# In[70]:


bool_of_active[bool_of_active=='0']='inactive'
bool_of_active[bool_of_active=='500']='active'


# In[71]:


bool_of_active


# In[53]:


np.unique(mood)


# In[54]:


np.unique(mood, return_counts=True)


# In[55]:


np.mean(step_count)


# In[56]:


np.max(step_count)


# In[57]:


np.argmax(step_count)


# In[58]:


date[np.argmax(step_count)]


# In[59]:


data[np.argmax(step_count)]


# In[60]:


calories_burned[np.argmax(step_count)]


# In[62]:


np.unique(mood[step_count>4000], return_counts=True)


# In[65]:


np.mean(hours_of_sleep)


# In[67]:


np.unique(mood[hours_of_sleep<5.2], return_counts=True)


# In[68]:


np.unique(mood[hours_of_sleep<4], return_counts=True)


# In[72]:


np.unique(bool_of_active[hours_of_sleep<4], return_counts=True)


# In[73]:


np.unique(bool_of_active[hours_of_sleep>5], return_counts=True)


# In[75]:


weight_kg = np.array(weight_kg, dtype='int')


# In[76]:


weight_kg


# In[ ]:





# Different concept

# In[ ]:





# In[77]:


arr = np.array([-3,4,27,34,-2, 0, -45,-11,4, 0 ])
arr


# In[81]:


arr[arr>0]=1
arr[arr<0]=-1


# In[82]:


arr


# Similar action can be done by below

# In[84]:


arr = np.array([-3,4,27,34,-2, 0, -45,-11,4, 0 ])


# In[85]:


np.where(arr>0, 1, -1)


# Difference is the application of logic. Earlier one equal to zero's will stay as such while in the later equal to zero's will also be updated.

# In[ ]:





# ### Matrix multiplication

# In[86]:


a = np.array([2,3,4,5])
b = np.array([3,4,5,6])


# ' * ' is element-wise multiplication

# In[87]:


a*b


# For matrix multiplication, '@', 'matmul' and 'dot' can be used.

# In[88]:


a=np.arange(1,10).reshape((3,3))


# In[89]:


a


# In[90]:


b=np.arange(2,11).reshape((3,3))


# In[91]:


b


# In[92]:


np.matmul(a,b)


# In[93]:


np.matmul(b,a)


# In[94]:


a@b


# In[95]:


np.dot(a,b)


# In[96]:


np.dot(4,5)


# In[101]:


d= np.arange(1,5)
d


# In[104]:


e=np.arange(2,6)


# In[105]:


e


# In[106]:


np.dot(d,e)


# In[107]:


np.matmul(d,e)


# In[113]:


get_ipython().run_line_magic('pinfo', 'np.matmul')


# In[114]:


get_ipython().run_line_magic('pinfo', 'np.dot')


# In[116]:


g=np.arange(1,13).reshape((3,4))
g


# In[117]:


h=np.arange(1,13).reshape((4,3))
h


# In[118]:


np.dot(g,h)


# In[119]:


np.dot(h,g)


# In[120]:


j=np.arange(1,4).reshape((1,3))
h=np.arange(1,16).reshape((3,5))
print(j)
print(h)


# In[121]:


np.dot(j,h)


# In[122]:


np.dot(h,j)


# In[123]:


h=np.arange(1,16).reshape((5,3))
print(h)


# In[124]:


j.shape


# In[125]:


np.dot(j, h.T)


# In[ ]:





# In[126]:


#np.tile()


# In[127]:


t=np.arange(1,13).reshape((3,4))
t


# In[128]:


np.tile(t,(2,2))


# In[129]:


np.tile(t,(3,2))


# In[ ]:





# In[130]:


a=np.array([1,2,3,4,5])
b=np.array([8,7,6])


# In[131]:


a[2:] = b[::-1]


# In[132]:


a


# In[134]:


a=np.array([1,2,3,4,5])
b=np.array([8,7,6])


# In[135]:


a[1:] = b[::-1]
a


# In[ ]:




