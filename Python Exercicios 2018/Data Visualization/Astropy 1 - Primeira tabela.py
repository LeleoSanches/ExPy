
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


from matplotlib import pyplot as plt


# In[7]:


from astropy.table import Table


# In[8]:


a = [1, 4, 5]
b = [2.0, 5.0, 8.2]
c = ['x', 'y', 'z']
q = Table([a, b, c], names=('a', 'b', 'c'), meta={'name':'Primeira tabela'})


# In[10]:


print (q)

