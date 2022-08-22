#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'prime2.py', 'def prime_interval(x,y):\n    prime_list = []\n    for i in range(x,y):\n        if i == 0 or i == 1:\n            continue\n        else:\n            for j in range(2, int(i/2)+1):\n                if i % j == 0:\n                    break\n            else:\n                prime_list.append(i)\n    return prime_list')


# In[4]:


get_ipython().run_cell_magic('writefile', '-a prime2.py', 'prime_interval(10,20)')


# In[2]:


def prime_interval(x,y):
    prime_list = []
    for i in range(x,y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


# In[3]:


prime_interval(10,20)


# In[ ]:




