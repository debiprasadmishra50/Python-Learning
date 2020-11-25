#!/usr/bin/env python
# coding: utf-8

# ## Functions and Methods

# #### Methods are defined in classes and objects, functions are defined outside

# In[1]:


string = "Debi Prasad"


# In[4]:


capital_string = string.upper()


# In[3]:


string


# In[5]:


capital_string


# In[6]:


help(string.split)


# In[12]:


helloworld()

def helloworld():    #Function helloworld Created
    print("Hello, Function!")

helloworld()


# In[11]:


helloworld


# ### Input and Return

# In[13]:


def hello_program(name):
    print("Hello Python")
    print(f"I am {name} and I am learning python")


# In[15]:


hello_program("Debi Prasad")


# In[17]:


hello_program()


# In[18]:


def func(name="Debi Mishra"):
    print("Hello Python")
    print(f"I am {name} and I am learning Python")


# In[21]:


func("ROck")


# In[22]:


def add(num1, num2):
    num3 = num1 + num2
    print(f"Sum of 2 numbers are : {num3}")


# In[24]:


res = add(10,20)


# In[28]:


type(res)


# In[29]:


def summation(num1, num2, num3):
    return num1+num2+num3


# In[30]:


summation(10,20,30)


# In[31]:


res = summation(10,20,30)


# In[32]:


res


# In[33]:


type(res)


# In[35]:


def string_control(s):
    if s[0] == "m":
        print(s.capitalize())


# In[36]:


string_control("monkey")


# In[38]:


string_control("lucky")


# ### arbitrary argument and key-word argument

# In[47]:


def summation2(*args):  # You can pass any argument and any number of argument
    return sum(args)


# In[42]:


summation2(10,20,30)


# In[43]:


summation2(12,3,5,23,34,52,231)


# In[44]:


def args(*args):
    print(args)


# In[45]:


args(12,3,4,14,124,14,14)


# In[46]:


args("a", "b", 13, 1, 32)


# In[50]:


def keyword_func(**kwargs):  #Takes input as key=value pairing
    print(kwargs)


# In[51]:


keyword_func(run=100, badminton=200, swim=300)


# In[52]:


def key_func(**kwargs):
    if "run" in kwargs:
        print("You should run more")
    else:
        print("YOu play badminton")


# In[53]:


key_func(run=100, badminton=200, swim=300)


# ### Practical Usage

# In[54]:


def divide(num):
    return num / 2


# In[55]:


divide(10)


# In[56]:


number = [1,2,3,4,5,6,7,8]


# In[65]:


new_list = []
for item in number:
    new_list.append(divide(item))
print(new_list)


# #### Map Function

# In[63]:


list(map(divide, number))


# In[71]:


def string_func(string):
#     if "debi" in string:
#         return True
    return "debi" in string


# In[74]:


string_func("debi dsvdbvdijn")


# In[85]:


instrument_list = ["Guitar", "piano", "Banjo", "Drum", "Tabla", "debi prasad", "debi mishra"]


# In[86]:


list(map(string_func, instrument_list))


# ### Filter Function

# In[87]:


list(filter(string_func, instrument_list))


# In[ ]:




