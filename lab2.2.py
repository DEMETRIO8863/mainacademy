#!/usr/bin/env python
# coding: utf-8

# In[38]:


import random
import math
a = random.sample(range(100), 5)
b = random.random()
a1 = max(a)
num = (a1 - b)
num1 = (math.floor(num))
factorial = 1
if num1 < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num1 == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num1 + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
print(a)
print(b)
print(a1)
print (num1)



# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




