#!/usr/bin/env python
# coding: utf-8

# ## Lists
# #### Mutable : Use [ ] : Can Store Duplicate Values

# In[1]:


name = "Debi"


# In[2]:


name[0]


# In[3]:


name[1]
# name[1] = "M"


# #### Strings are Immutable

# ### Lists are mutable and declared as [ ]

# In[27]:


number = [1,2,3,4]


# In[28]:


number


# In[29]:


number[0] = 5


# In[30]:


number


# In[31]:


number[2]


# In[32]:


number.append(5) # Append data in last


# In[33]:


number


# In[34]:


number.count(5) # Count how many numbers of this data are present


# In[35]:


number.pop() # Remove the last item by default, if argument given, removes the index value = argument


# In[36]:


number


# In[37]:


number.pop(1)


# In[38]:


number


# In[58]:


new_list = [1,2,"Debi","Prasad"]


# In[59]:


new_list


# In[41]:


new_list[-1]


# In[61]:


new_list[::-1]


# In[44]:


list2 = [2,4,5,"New List"]


# In[46]:


Added_List = new_list + list2


# In[47]:


Added_List


# In[48]:


new_list * 3


# In[62]:


new_list


# In[64]:


new_list.reverse()


# In[65]:


new_list


# ## List Advanced

# #### Nested List

# In[66]:


new_list = [1,2,"a"]


# In[67]:


new_list = [1,2,"a",[3,"b"]]


# In[68]:


new_list


# In[69]:


new_list[3]


# In[70]:


nested_list = new_list[3]


# In[74]:


nested_list[1]


# In[75]:


new_list[3][1] # FInding element in nested list


# In[76]:


new_list[2:]


# In[77]:


new_list[:2]


# In[81]:


new_list


# In[ ]:




