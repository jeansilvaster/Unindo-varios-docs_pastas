#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import os


# ### Lendo arquivos

# In[19]:


path = r'C:\PYTHON\Estados'
files = os.listdir(path)
df = pd.DataFrame()


# In[20]:


print(files)


# In[27]:


files_xlsx = [path +'\\' + f for f in files if f[-4:]== 'xlsx']
print(files_xlsx)


# In[31]:


for f in files_xlsx:
    data = pd.read_excel(f)
    df = df.append(data)


# In[32]:


df

