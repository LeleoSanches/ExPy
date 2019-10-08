
# coding: utf-8

# In[1]:


from astropy.table import Table


# In[4]:


data_rows = [(1, 2.0, 'x'), (4, 5.0, 'y'), (5, 8.2, 'z')]


# In[7]:


t = Table(rows=data_rows, names=('a', 'b', 'c'), meta={'name':'primeira tabela'})


# In[8]:


print (t)


# In[9]:


t

