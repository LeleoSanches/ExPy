
# coding: utf-8

# In[3]:


import pandas as pd
from astropy.table import QTable
from matplotlib import pyplot as plt


# In[2]:


from astropy.io import ascii


# In[9]:


data = ascii.read('file:///C:/Users/Leona/Desktop/UGC07603_rotmod.dat')


# In[10]:


data


# In[29]:


Raio = data['col1']
Vstars = data['col2']
erro = data['col3']


# In[37]:




