
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


d = {'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]}
df = pd.DataFrame(data=d)


# In[6]:


df['mean'] = (df['A'] + df['B']) / 2


# In[9]:


df

