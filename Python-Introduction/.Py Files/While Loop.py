#!/usr/bin/env python
# coding: utf-8

# ## While Loop

# In[4]:


num = 5


# In[5]:


while (num > 0):
    print(num)
    num-=1


# In[6]:


num = [1,2,3,4,5]


# In[7]:


num.pop()


# In[8]:


num


# In[9]:


num.append(5)


# In[10]:


num


# while 3 in num:
#     print("3 is in the list")
#     num.pop()

# In[16]:


number = 0


# In[17]:


while number < 10:
    if number == 5:
        break
    print(number)
    number = number + 1


# In[28]:


p = 0
while p < 20:
#     print("Value of p : "+str(p))
    print(f"Value of p : {p}") # Formatting
    p += 1

