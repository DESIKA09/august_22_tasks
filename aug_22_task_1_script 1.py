#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'prime1.py', 'def prime(x):\n    prime_list = []\n    for i in range(0,x):\n        if i == 0 or i == 1:\n            continue\n        else:\n            for j in range(2, int(i/2)+1):\n                if i % j == 0:\n                    break\n            else:\n                prime_list.append(i)\n    return prime_list')


# In[2]:


get_ipython().run_cell_magic('writefile', '-a prime1.py', 'prime(10)')


# In[3]:


def prime(x):
    prime_list = []
    for i in range(0,x):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


# In[4]:


prime(10)


# In[ ]:




