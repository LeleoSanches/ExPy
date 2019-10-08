
# coding: utf-8

# In[5]:


from astropy.table import QTable


# In[6]:


import astropy.units as u


# In[10]:


t = QTable()
t['distancia'] = [1, 2]* u.m
t['velocidade'] = [3, 4] *u.m / u.s


# In[11]:


t

