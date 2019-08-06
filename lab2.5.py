#!/usr/bin/env python
# coding: utf-8

# In[24]:


Countris = {'Ukraine':'UA','Russia':'RU','USA':'US','Great Britain':'GB','Czech':'CZ'}
Capitals = {'Russia':'Moscow','Ukraine':'Kyiv','USA':'Washingtone','Great Britain':'Londone','Czech':'Prague'}
Capitals['Belgium'] = "Brussels"
Countris['Belgium'] = "BG"
for country in Capitals:
    if country in Capitals:
        print('Столица' + country + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)
i = 'US'
while i in Countris:
    print('Столица ' + i)
    i = i*2
print(i)
print(Countris)
print(Capitals)


# In[18]:


Capitals = dict()

Capitals['Russia'] = 'RU'
Capitals['Ukraine'] = 'UA'
Capitals['USA'] = 'US'
Capitals['Great Britain'] = 'GB'
Capitals['Czech'] = 'CZ'

Countries = ['Russia', 'France', 'USA', 'Russia','Czech', 'Great Britain']
for country in Countries:
    if country in Capitals:
        print('Domaine name ' + country + ': ' + Capitals[country])
    else:
        print('В базе нет страны c названием ' + country)


# In[ ]:





# In[ ]:




