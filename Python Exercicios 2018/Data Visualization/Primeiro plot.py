
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[6]:


x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x, y) # Plota os valores
plt.plot(x, z) # Plota os valores
plt.title("Test Plot") # Nome do gráfico
plt.xlabel("x") # Nome do eixo x
plt.ylabel("y") # Nome do eixo y
plt.legend(["this is y", "This is z"]) #Legenda dos plots
plt.show()


# In[7]:


sample_data = pd.read_table("test.dat")


# In[8]:


sample_data

