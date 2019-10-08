
# coding: utf-8

# In[1]:


import pandas as pd


# In[23]:


from astropy.table import QTable


# In[3]:


from matplotlib import pyplot as plt


# In[24]:


a = [1, 2, 3, 4, 5]
b = [3, 5 ,7, 8, 10]
t = QTable([a, b], meta={'name':'tabela1'})


# In[32]:


plt.plot(a, b, 'ro') # Plota os valores
plt.title("Test Plot") # Nome do gráfico
plt.xlabel("x") # Nome do eixo x
plt.ylabel("y") # Nome do eixo y
plt.show()


# In[36]:


plt.plot(t['col0'], t['col1'], 'ro') # Plota os valores
plt.title("Test Plot") # Nome do gráfico
plt.xlabel("x") # Nome do eixo x
plt.ylabel("y") # Nome do eixo y
plt.show()


# In[35]:




