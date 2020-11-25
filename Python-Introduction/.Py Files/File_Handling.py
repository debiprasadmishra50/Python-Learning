#!/usr/bin/env python
# coding: utf-8

# ## File Handling

# In[1]:


get_ipython().run_cell_magic('writefile', 'file.txt', 'Test 1\nTest 2\nTest 3')


# In[2]:


content = open("file.txt")


# In[3]:


content.read()


# In[5]:


content.read() # Cursor is at end so it will show blank


# In[8]:


content.seek(0) # takes the cursor to beginning


# In[9]:


content.read()


# In[10]:


content.close() # Need to close else will get an error while deleting


# ### With Keyword 
# ### for mode => r = read, w = write, a = append

# In[11]:


with open("file.txt") as content:
    read_file = content.read()


# In[12]:


read_file


# In[13]:


read_file


# In[17]:


with open("file.txt", mode="r") as new_content:  # r = read, w = write, a = append
    new_file_read = new_content.read()


# In[15]:


new_file_read


# In[18]:


with open("file.txt", mode="w") as new_content:
    new_file_read = new_content.write("Test 4")


# In[19]:


with open("file.txt", mode="r") as new_content:  
    new_file_read = new_content.read()


# In[22]:


new_file_read  # Content Removed and changed to Test 4


# In[23]:


with open("file.txt", mode="a") as new_content:
    new_file_read = new_content.write("Test 5")


# In[24]:


with open("file.txt", mode="r") as new_content:  
    new_file_read = new_content.read()


# In[25]:


new_file_read  # Appended the Test 5


# In[ ]:




