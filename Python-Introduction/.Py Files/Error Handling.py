#!/usr/bin/env python
# coding: utf-8

# ## Error Handling : try, except, finally

# In[1]:


def add(num1, num2):
    return num1 + num2


# In[8]:


x = input("Enter 1st number : ")


# In[9]:


y = input("Enter 2nd Number : ")


# In[10]:


add(x,y) #This is concatenation as input is in the string format, you need to cast str into int


# In[11]:


x = int(x); y = int(y)


# In[7]:


add(x,y)


# In[12]:


def power(x):
    return x ** 2


# In[13]:


power(3)


# ### try, except, finally

# In[10]:


while True:
    try:
        number = int(input("Enter a number : "))
    except:
        print("Please enter valid input!")
        continue
    else:        # If user enters an integer, come to this else part
        print("OK")
        break
    finally:
        print("This is Finally Block\n")


# In[11]:


type(number)


# In[12]:


number


# In[ ]:




