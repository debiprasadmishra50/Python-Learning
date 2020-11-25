#!/usr/bin/env python
# coding: utf-8

# ## Special Methods : str, len, init

# In[54]:


class Fruits():
    
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    
    def __str__(self):
#         return f"{self.name} has {self.calories} calories"
        return f"({self.name}, {self.calories})"
    
    def __len__(self):
        return self.calories


# In[55]:


fruit = Fruits("banana", 200)


# In[56]:


fruit.name


# In[57]:


print(fruit)


# In[58]:


# len(fruit) # Will gimme an error
len(fruit)


# In[ ]:




