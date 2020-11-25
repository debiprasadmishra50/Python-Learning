#!/usr/bin/env python
# coding: utf-8

# ## Modules and Packages

# In[29]:


import numpy as np
import matplotlib.pyplot as matplot

grades = np.random.normal(80,30,1000)
np.mean(grades)


# In[30]:


matplot.hist(grades, 50)
matplot.show()


# ## Writing Own Moduels

# In[31]:


# Save this code in a test.py file
def func():
    print("This is a Function")

func()


# In[ ]:


# Create another .py file
from test import func()

func()

# Run it from Command Line


# ## Import and Direct

# In[ ]:


# Create 2 different .py file ; test.py and main.py

# test.py
def func_direct():
    print("test direct")

def func_import():
    print("test imported")

if __name__ = '__main__':    # If the function is called in the same file or class, then do this, if imported in another project, then do else
    func_direct()
else:
    func_import()

# main.py
import test

print("main.py")

# Run them from command line
# python test.py -> test direct
# python main.py -> test imported

