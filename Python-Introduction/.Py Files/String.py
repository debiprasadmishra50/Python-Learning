#!/usr/bin/env python
# coding: utf-8

# ##  Strings

# In[1]:


"Hello, World!"


# In[2]:


'Hello, World!'


# In[3]:


"I'm a developer"


# In[7]:


"He said \"Do not touch this\""


# In[20]:


x = "Hello, World!"


# In[15]:


x


# In[22]:


type(x)


# In[23]:


len(x)


# In[24]:


print(x)


# #### Escape Characters

# In[26]:


print("Hello \nPython")


# In[27]:


print("Hello \t Python")


# ## String Advanced

# In[30]:


string = "Hello, World!"


# In[31]:


string


# #####  Indexing

# In[33]:


string[0] #Index starts with 0


# In[36]:


string[4]


# In[38]:


string[-1]


# In[39]:


string[-2]


# In[46]:


numbers = "1234567890"


# In[43]:


numbers


# In[44]:


numbers[0]


# ###  Slicing

# In[47]:


numbers[1:]


# In[48]:


numbers[5:]


# In[49]:


numbers[3:7]


# In[50]:


numbers[:3]


# In[58]:


numbers[2:9:2] # Start : Stop : Increment


# In[59]:


numbers[::]


# In[60]:


numbers[::3]


# In[61]:


numbers[::2]


# In[64]:


# Reverse String
numbers[::-1]


# In[63]:


numbers[::1]


# ## String Methods

# In[67]:


name = "debi"


# In[73]:


name_capitalized = name.capitalize()


# In[72]:


name


# In[74]:


name_capitalized


# In[75]:


name.encode()


# In[78]:


name = "debi prasad"


# In[80]:


name_split = name.split()


# In[81]:


name_split


# In[84]:


name.find("p")


# In[85]:


name.upper()


# In[93]:


"Debi " * 10


# In[94]:


"Debi " + "5 " + "Mishra"


# In[96]:


first_name = "Debi"


# In[97]:


last_name = "Mishra"


# In[98]:


full_name = first_name + " " + last_name


# In[99]:


full_name


# In[ ]:




