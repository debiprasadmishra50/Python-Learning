#!/usr/bin/env python
# coding: utf-8

# ## Practice Examples

# In[73]:


for i in range(1,6):
    print("* " * i)
    


# In[71]:


for i in range(5,0,-1):
    print("* " * i)


# #### Reverse a number

# In[33]:


num = 1234; x = 0; rev_num = 0;
while(num > 0):
    x = num % 10
    rev_num = rev_num*10 + x
    num = num//10
print(f"Reversed Number is {rev_num}")


# #### arithmetic operation with user input

# In[45]:


a = input("Enter 1st number : ")
b = input("Enter 2nd Number : ")
a = int(a); b = int(b);

print(f"Addition is : {a+b}")
print(f"Subtraction is : {a-b}")
print(f"Multiplication is : {a*b}")
if b > 0:
    print(f"Division is : {a/b}")
else:
    print("Cannot divide by zero")


# In[70]:


for i in range(1,6):
    for j in range(1,i):
        print(f"{j} ", end="")
    print("")


# In[69]:


for i in range(1,6):
    for j in range(0,i):
        print(f"{i} ", end="")
    print("")


# In[65]:


for i in range(1,6):
    for j in range(0,i):
        print(f"{i+j} ", end="")
    print("")


# In[74]:


for i in range(1,6):
    print("* " * i)
for i in range(6, 0, -1):
    print("* " * i)


# In[75]:


for i in range(6, 0, -1):
    print("* " * i)
for i in range(1,6):
    print("* " * i)


# In[92]:


# Fibonacci Sequence
a = 1; b = 1
print('First 10 Fibonacci Number')

for i in range(1, 6):
    print(f"{a} {b}", end=" ")
    a = a + b
    b = a + b

