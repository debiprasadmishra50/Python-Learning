#!/usr/bin/env python
# coding: utf-8

# ## Dictionary
# #### Mutable and denoted by {key, value}
# #### Key Value Pair 	: Use {} 	: Mutable : Can Store Duplicate Values

# In[1]:


dictionary = {"key":"value"}


# In[2]:


dictionary


# In[3]:


dictionary["key"]


# #### Creating a fitness list
# 

# In[4]:


fitness = [100,200]


# In[5]:


new_list = ["run", "swim"]


# In[6]:


fitness[0]


# In[7]:


new_list[0]


# In[8]:


dict_fitness = {"run":100, "swim":200}


# In[9]:


dict_fitness


# In[10]:


dict_fitness["run"]


# In[11]:


dict_fitness["swim"]


# In[16]:


# MIXED Data-structure in Dictionary
my_new_dict = {"key1":1, "key2":2, "key3":"Apple"}


# In[13]:


my_new_dict


# In[14]:


my_new_dict["key1"]


# In[15]:


my_new_dict["key3"]


# In[17]:


dict_3 = {"key1":1, 2:5}


# In[18]:


dict_3["key1"]


# In[19]:


dict_3[2]


# In[20]:


data_dict = {"key1":100, "key2":[10,20,30], "key3":{"a":5}}


# In[21]:


data_dict


# In[22]:


data_dict.items()


# In[23]:


data_dict.keys()


# In[24]:


data_dict.values()


# In[25]:


data_dict["key3"]["a"]


# In[26]:


data_dict["key1"] = 500


# In[27]:


data_dict["key1"]


# In[31]:


# Add another element to Dictionary
data_dict["key4"] = 1234


# In[29]:


data_dict


# In[ ]:




