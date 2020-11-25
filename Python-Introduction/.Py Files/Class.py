#!/usr/bin/env python
# coding: utf-8

# ## Class

# In[2]:


new_list = list()


# ### Instance & attributes

# ### Create User Defined Class

# In[10]:


class Name():
    
    def __init__(self, name, age): #Initializer Function, like a constructor in JAVA, will take argument from user while instantiation
        self.name_attribute = name
        self.age_attribute = age


# In[11]:


name = Name("Debi", 20)


# In[12]:


name.age_attribute


# In[13]:


name.name_attribute


# In[14]:


name.name_attribute = "Mishra"


# In[15]:


name.name_attribute


# In[16]:


class Name():
    
    def __init__(self, name, age, sport): #Initializer Function, like a constructor in JAVA
        self.name = name
        self.age = age
        self.sport = sport


# In[17]:


Object = Name("Debi", 20, "Badminton")


# In[19]:


print(f"{Object.name} -> {Object.age} -> {Object.sport}")


# ### Default value to attribute

# In[28]:


class Animal():
    
    price = 50 #Default Variable
    
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed


# In[29]:


animal = Animal("pitbull", 10, "royal")


# In[30]:


animal.price


# In[31]:


print(f"{animal.name} {animal.age}year {animal.breed}breed {animal.price}Dollars")


# In[34]:


animal.price = 40 #Changing default variables


# In[35]:


print(f"{animal.name} {animal.age}year {animal.breed}breed {animal.price}Dollars")


# ## Methods inside Class

# In[43]:


class Vehicle():
    
    wheel = 4
    
    def __init__(self, name, year, fuel):
        self.name = name
        self.year = year
        self.fuel = fuel
    
    #Methods
    def run(self):
        print(f"This car is cool, it runs on {self.fuel}")


# In[44]:


car = Vehicle("Ferrari", 2020, "Gasoline")


# In[45]:


car.run()


# ### Practical Examples

# In[75]:


class DogYears():
    
    year_factor = 7
    
    def __init__(self, age=5):
        self.age = age
        self.name = "Husky"
        self.age_multiplied = age * self.year_factor
    
    def calculation(self):
        return self.age * DogYears.year_factor


# In[76]:


dog = DogYears(2)


# In[77]:


dog.calculation()


# In[78]:


dog_2 = DogYears()


# In[79]:


dog_2.calculation()


# In[80]:


dog.name


# In[81]:


dog.age_multiplied


# In[82]:


dog_2.age_multiplied


# ## Inheritance

# In[90]:


class Class1():
    
    def __init__(self):
        print("Class-1 Created")
    
    def method_1(self):
        print("Class-1 Method-1")
    
    def method_2(self):
        print("Class-1 Method-2")


# In[91]:


instance = Class1()


# In[92]:


instance.method_1()


# In[93]:


instance.method_2()


# In[101]:


class Class2(Class1): # Inheritance
    
    def __init__(self):
        Class1.__init__(self) #init() method of Class1 Called
        print("Class-2 Created")
    
    def method_3(self):
        print("Class-2 method-2")
    
    # Override
    
    def method_1(self):
        print("Class-2 method-1; Over-ridden method")


# In[102]:


inst2 = Class2()


# In[103]:


inst2.method_1()


# In[104]:


inst2.method_3()


# In[105]:


inst2.method_1()


# In[106]:


instance.method_1()


# In[ ]:




