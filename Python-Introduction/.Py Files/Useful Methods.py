#!/usr/bin/env python
# coding: utf-8

# ## Useful Methods - range, enumerate, random, zip

# In[1]:


number = [1,2,3,4,5,6]


# In[3]:


for num in number:
    print(num)


# ### range() method

# In[7]:


list(range(10))


# In[8]:


for num in list(range(10)):
    print(num)


# In[9]:


for num in list(range(5,10)):
    print(num)


# In[10]:


for num in list(range(0, 20, 2)):
    print(num)


# ### enumerate() Method

# In[14]:


index = 0
for num in list(range(10, 20)):
    print(f"Index : {index} --> Number : {num}")
    index+=1


# In[15]:


for num in enumerate(list(range(10,20))):
    print(num)


# In[19]:


for (index,num) in enumerate(list(range(10,20))):
    print(f"{index} --> {num}")


# ### Random

# In[20]:


from random import randint


# In[32]:


randint(0, 10)


# In[35]:


number = list(range(1,20))


# In[36]:


number


# In[37]:


from random import shuffle


# In[38]:


shuffle(number)


# In[39]:


number


# ### Zip - Merge multiple lists

# In[42]:


sport = ["run", "swim", "badminton"]


# In[43]:


calories = [100, 200, 300]


# In[44]:


day = ["monday", "tuesday", "wednessday"]


# In[45]:


new_list = list(zip(sport, calories, day))


# In[46]:


new_list


# In[47]:


for element in new_list:
    print(element)


# ## List Advanced

# In[1]:


my_list = []
string = "Debi Prasad"

for element in string:
    my_list.append(element)


# In[2]:


my_list


# In[3]:


new_list = [element for element in string]


# In[4]:


new_list


# In[8]:


number_list = [num*2 for num in list(range(0,20))]


# In[9]:


number_list


# In[ ]:




