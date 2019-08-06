#!/usr/bin/env python
# coding: utf-8

# In[3]:





# In[4]:


#створіть список із 100 чисел(заповніть їх рандомно). реалізуйте алгоритм сортування бульбашкою
from random import randint
 
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)
 
 
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
 
print(a)


# In[ ]:




