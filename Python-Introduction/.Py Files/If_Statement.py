#!/usr/bin/env python
# coding: utf-8

# ## If Statement

# In[8]:


if 3 > 2:
    print("3 is greater")
    print("Python is good")
else:
    print("2 is greater")


# In[10]:


x = 5


# In[20]:


y = 5


# In[21]:


if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("y is greater")


# In[22]:


name = input("Enter your name : ")


# In[26]:


if name == "Debi":
    print("Name is Debi")
elif name == "Mishra":
    print("Name is Mishra")
else:
    print("Name is not entered or can not display name")


# In[29]:


a = 10; b = 20; c = 30


# In[34]:


if a > b or b > c:
    print("Yo Hoo")
elif a < b or b > c:
    print("Aa Haa")


# In[38]:


isDead = False;
if isDead == True:
    print("Character is Dead")
else:
    print("Character is Alive")


# In[39]:


if isDead:    # Will consider isDead as True as in "if isDead == True"
    print("Character is Dead")
else:
    print("Characer is Alive")


# In[42]:


if not isDead:  # isDead is True by Default, not isDead becomes False
    print("Character is Alive")


# In[43]:


string = "Hello, World!"


# In[47]:


if string == "Hello, World!":
    print("Equal")
else:
    print("Not Equal")


# In[48]:


if "Hello" in string:
    print("True")
else:
    print("False")

