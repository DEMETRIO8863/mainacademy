#!/usr/bin/env python
# coding: utf-8

# In[12]:


a = input('Введіть число')
#
print(len(a))
#
summa = 0
for i in range(len(a)):
    summa = summa +int(a[i])
print(summa)
#
print(a-[1])
    


# In[22]:


a = [1,2,3,4,5,6,7,8,9,10,11,12]
#
k = 0
for i in a:
    if i % 2 !=0:
        k = k + 1
print(k)
#
k = 0
for i in a:
    if i % 2 !=0 and i<0:
        k = k + 1
print(k)
#
print(max(a))
#
b=[]
for i in a:
    if i % 2 != 0:
        b.append(i)
print(max(b))
#
for i in range(len(a)):
    if a[i]>10:
        a[i] = 10
print(a)


# In[ ]:




