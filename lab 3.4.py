#!/usr/bin/env python
# coding: utf-8

# In[1]:


year = int(input())
if year % 4 != 0:
    print("usual year")
elif year % 100 == 0:
    if year % 400 == 0:
        print("intercalary year")
    else:
        print("usual year")
else:
    print("intercalary year")


# In[ ]:




