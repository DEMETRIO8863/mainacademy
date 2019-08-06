#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
a = int(input())
b = int(input())
c = math.sqrt(a**2 + b**2)
print (c)


# In[2]:


a = int(input())
b = int(input())

if a>b:
    print(a)
else:
    print(a,b)


# In[9]:


t = input()
lenght = len(t)
pokaznyk = t[lenght - 1]
temp = t [0:lenght - 1]
if pokaznyk =='C':
    t = 5/9*(float(temp)-32) 
    print(str(t)+"F")
else:
    t=9/5*float(temp)+32
    print(str(t)+"C")


# In[10]:


parametr = input()
if parametr == 's':
    v = int(input('введите скорость'))
    t = int(input('введите час'))
    s = v*t
    print(s)
elif parametr =='v':
    s = int(input("введите растояние"))
    t = int(input('введите час'))
    v = s/t
    print(v)
else:
    s = int(input("введите растояние"))
    v = int(input('введите скорость'))
    t = s/v
    print(t)
    


# In[ ]:


x = int(input('введите число'))
y = int(input("введите следующе число"))
a = (x+y)/2
b = 2*x*y
if x>y:
    print(x,a)
else:
    

