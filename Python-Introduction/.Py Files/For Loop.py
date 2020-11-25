#!/usr/bin/env python
# coding: utf-8

# ## For Loop

# In[1]:


number = [1,2,3,4,5]


# In[2]:


for num in number:
    print(num)


# In[3]:


for no in number:
    new_no = no * 5
    print(new_no)


# In[5]:


for num in number:
    if num % 2 == 0:
        print(str(num)+" is Even")
    else:
        print(str(num)+" is Odd")


# In[6]:


string = "Debi Prasad"


# In[7]:


for letter in string:
    print(letter)


# In[10]:


for num in range(1, 10, 3):
    print(num)


# ## Break Continue Pass

# In[11]:


number = [10, 20, 30, 40, 50, 60]


# In[17]:


for num in number:
    if num == 30:
        continue
    print(num)


# In[15]:


for num in number:
    if num == 40:
        break
    print(num)


# In[20]:


for num in number:
    pass  # It will pass the code if you have any error

