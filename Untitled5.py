#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.'''
s = 'Abrakadabra'
t = '0'
for i in range(0,len(s)):
    if i %3 != 0:
        t = t + s[i]
print(t)


# In[ ]:




