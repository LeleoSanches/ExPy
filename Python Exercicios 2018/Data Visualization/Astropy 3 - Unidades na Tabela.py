
# coding: utf-8

# In[1]:


from astropy.table import Table


# In[2]:


data_rows = [(1, 2.0, 'x'), (4, 5.0, 'y'), (5, 8.2, 'z')]


# In[3]:


t = Table(rows=data_rows, names=('a', 'b', 'c'), meta={'name':'primeira tabela'})


# In[5]:


t['a'].unit = 'Metros'
t['b'].unit = 'Grama'
t['c'].unit = 'Variavel'


# In[6]:


t

