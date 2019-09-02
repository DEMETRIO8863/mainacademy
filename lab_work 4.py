#!/usr/bin/env python
# coding: utf-8

# In[3]:


#lab_work 4.2
set1 = list(range(10))  
set2 = list(range(0,10,2))  
result = [] 

def function (set1, set2):
    result = []
    for j in set1: 
        if j in set2: 
            result.append(j) 
    return result

print(function(set1, set2))
print("List:", result)


# In[5]:


#lab_work 4.3
word = 'Found name:'  
IDS = {'name':"Alice", 'age':27}  

def function(word, name, *args, age=None): 
    print(word, name) 
    print('Age:',age) 
    print(args)     

function(word, **IDS) 
function(word, IDS['name'], *list(range(10)))


# In[18]:


#lab_work 4.4
foo = [1, 2, 3, 4, 5]
odd_foo = [x for x in foo if x % 2 == 1]
odd_foo = filter(lambda x: x % 2 == 1, foo)  
print(list(filter(lambda x: x % 2 == 1, foo)))


# In[14]:


#Lab_4_5_generators.py    
lst = [1, 2, 3, 4, 5]
def my_function(lst):   
    for item in lst:     
        yield lst.index(item)+1, item  
for item in my_function(lst):
    print(item)


# In[26]:


#lab_work 4.6
companies = ["Microsoft", "Google", "Oracle", "Apple"]

def decorrator(func):
    def decorrator(item):
        data_file = open("config.data", "r+")
        func(data_file, item)
        data_file.close()
    return decorrator
        

@decorrator
def writeConfig(file, line):   
    if "Configuration file! Do not modify!" in file.read():
        file.write("%s;\n"%(line))
    else:
        file.write("Configuration file! Do not modify! \n"+                    "%s; \n" % (line))

        
for item in companies:
    writeConfig(item)


# In[ ]:




