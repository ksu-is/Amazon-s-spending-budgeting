
# In[1]:


import pandas as pd


# In[2]:


orders = pd.read_csv('amazon_order_history.csv')


# In[ ]:





# In[3]:


orders.shape


# In[4]:


orders.columns


# In[5]:


orders = orders[orders.total != '1 Audible Credit']
orders.head()


# In[6]:


orders['total'] = orders['total'].replace('[CDN$, .]', '', regex=True)


# In[7]:


orders['total']


# In[8]:


orders.drop([53], axis=0, inplace=True)
orders['total'].tail()
#orders['total'] = orders['total'].astype(float)


# In[9]:


orders['total'] = orders['total'].astype(float)


# In[10]:


orders['total'] = orders['total'] / 100


# In[11]:


orders['total'].sum()


# In[12]:


orders['total'].mean()


# In[13]:


orders['total'].median()


# In[14]:


orders['total'].max()


# In[15]:


orders['total'].min()


# In[16]:


orders.head()


# In[17]:


orders.drop(['order id', 'to', 'gift', 'refund', 'VAT', 'payments'], axis=1, inplace=True)


# In[18]:


orders['date'] = pd.to_datetime(orders['date'])


# In[19]:


orders.head()


# In[20]:


import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


orders.plot.bar(x='date', y='total', figsize=(20,10))


# In[22]:


daily_orders = orders.groupby('date').sum()['total']


# In[23]:


daily_orders.plot.bar(figsize=(20,10), color='#8E44AD')
daily_orders


# In[24]:


orders['month'] = orders['date'].map(lambda x: x.month)
orders['month']


# In[26]:


orders['check'] = pd.Series([1])
orders.fillna(1, inplace=True)


# In[27]:


monthly_orders = orders.groupby('month').sum()['check']
monthly_orders.plot.bar(figsize=(20,10), color='#00FFFF', title='Number of Purchases per Month')


# In[28]:


monthly_totals = orders.groupby('month').sum()['total']
monthly_totals.plot.bar(figsize=(20,10), color='#6633FF', title='Amount Spent per Month')


# In[29]:


monthly_totals.mean()


# In[30]:


monthly_orders.mean()


# In[ ]:




