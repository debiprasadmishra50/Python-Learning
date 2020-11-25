#!/usr/bin/env python
# coding: utf-8

# ## Scope

# In[1]:


number = 10

def multiply(num):
    number = 5
    return num * number


# In[2]:


multiply(10)


# In[3]:


print(number)


# ## LEGB rule
# ## L = Local
# ## E = Enclosing
# ## G = Global
# ## B = Built-in

# In[10]:


string = "Debi"
#GLOBAL

def func():
    string = "Mishra"
    #ENCLOSING
    
    def func2():
        #LOCAL
        string = "Prasad"
        print(string)
    func2()


# In[11]:


func()


# In[12]:


string


# #### Change value of global variable

# In[24]:


y = 10

def new_func(y):
    print(y)
    y = 5
    print(y)
    return y


# In[25]:


new_func(10)


# In[26]:


y = new_func(y)


# In[27]:


y


# In[28]:


# OR Do this
y = 10

def function():
    global y
    y = 5
    print(y)


# In[29]:


function()


# In[30]:


y


# In[ ]:




