#!/usr/bin/env python
# coding: utf-8

# In[4]:



'''
Дана строка. 
Если в этой строке буква f встречается 
только один раз, выведите её индекс. 
Если она встречается два и более раз, 
выведите индекс её первого и последнего 
появления. Если буква f в данной строке 
не встречается, ничего не выводите.
'''
S = 'Pythonforever'
i = 'f'
Sf = S.find(i)
Srf = S.rfind(i)


for i in S:

    if Sf == -1:
        break   

    elif Sf == Srf:
        print("'f' в S есть. ")
        print("индекс появления 'f': ")
        print(Sf)
        break

    elif Sf != Srf:
        print("'f' в S есть. ")
        print("индекс появления 'f': ")
        print(Sf)
        print(Srf)
        break
        
    else:
        pass


# In[ ]:




