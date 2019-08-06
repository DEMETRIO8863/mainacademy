#!/usr/bin/env python
# coding: utf-8

# In[47]:


file= open('myfile.txt','r')
print(file.read())


# In[48]:


file = open('myfile.txt','w+')
text = file.read()
print(text)


# In[53]:


file = open('myfile.txt','w')
a = ('my')
file.write('Hello '+ str(a) + ' file')
file.close()



# In[ ]:





# In[ ]:




