#!/usr/bin/env python
# coding: utf-8

# In[1]:


set1 = {13,44,56,77,99,'a','b','c'}
set2 = {a*2 for a in set1}
set2.add(34)
print(set1)
print(set2)
intertup = tuple(set1&set2)
print("inter is ", intertup)
difertup = tuple(set1-set2)
print("diff is ", difertup)
print(intertup[0:2])
for a in set2:
    if str(a).isdigit():
        print(a,end=",")
print('/n')
print(difertup[::-1])
listtup1 = list(intertup)
listtup1.extend(list(difertup))
print(listtup1)


# In[ ]:




