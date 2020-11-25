#!/usr/bin/env python
# coding: utf-8

# ## Tuples
# #### Like List : Use () : Immutable : Can Store Duplicate Values

# In[1]:


my_tuple = tuple() #Empty Tuple


# In[4]:


my_list = ["a",1,"b"]


# In[5]:


my_list


# In[43]:


my_tuple = ("a",1,"b",1)


# In[44]:


my_tuple[0]


# In[28]:


# my_tuple[0] = "c"  # 'tuple' object does not support item assignment


# In[34]:


#Change the tuple into list to make it mutable
my_tuple = list(my_tuple)


# In[30]:


type(my_tuple)


# In[31]:


my_tuple


# In[32]:


my_tuple[0] = "c"


# In[35]:


my_tuple


# In[45]:


type(my_tuple)


# In[46]:


my_tuple


# In[47]:


my_tuple.count("a") # Count Number of occurances


# In[48]:


my_tuple.index("b")


# In[49]:


my_tuple[3] 


# In[ ]:




