#!/usr/bin/env python
# coding: utf-8

# ## Sets
# #### Hold Unique Values : Duplicate data can not be there
# #### Declared by variable_name = set() or using { } like dictionary but no "key":"value" pair
# #### Using set() method to a Variable : Holds Unique values, no duplicacy : Use {} : set1 = {1,2,3,4}

# In[1]:


my_list = [1,2,3,4,1,2,1]


# In[2]:


my_list


# #### Casting

# In[3]:


my_list = set(my_list)


# In[4]:


my_list


# In[8]:


set_2 = {1,2,3,4,1,2,3}


# In[9]:


set_2


# In[10]:


type(set_2)


# In[11]:


new_set = {"a", "b", "a", "c", "a"}


# In[12]:


new_set


# ##### Create Empty Set, list, dict, tuple, string

# In[23]:


a = set()


# In[24]:


type(a)


# In[35]:


a = {} #dict()


# In[34]:


type(a)


# In[28]:


a = [] #list()


# In[29]:


type(a)


# In[31]:


a = "" #str()


# In[32]:


type(a)


# In[38]:


a = () #tuple()


# In[39]:


type(a)


# In[ ]:




