#!/usr/bin/env python
# coding: utf-8

# I prevously installed **Pandas** using the command: "pip install pandas" via *Anaconda prompt*

# In[19]:


pwd


# In[20]:


import pandas as pd


# In[21]:


# reading the csv data file with url:
df = pd.read_csv("https://osf.io/7gvz9//download") 


# In[22]:


df.head()
# head() prints the first five rows by default; alternatively, one can set the number of rows as follows: head(#_of_rows


# In[23]:


# generating a list from the column "area" to apply 'word_count' function to it later on
area_list = df['area'].tolist()


# In[24]:


df['area_list'] = area_list


# In[25]:


df.head(10).area_list


# In[26]:


# creating a function 'word_count':
def word_count(abc):
    counter = {}
    for word in abc:
        if word in counter:
            # print('Increment:', word)
            counter[word] = counter[word] + 1
        else:
            # print('First time:', word)
            counter[word] = 1
        # print(counter)
    return counter


# In[27]:


word_count(area_list)


# ```There are 327 used cars from Chicago and 222 from Los Angeles in the dataset```

# In[28]:


for name, values in df.iteritems():
    print('{name}: {value}'.format(name=name, value=values[0]))


# In[29]:


for ind, column in enumerate(df.columns):
    print(ind, column)


# In[30]:


age_list = df['age'].tolist()


# In[31]:


old_new = ['new' if n < 8 else 'old' for n in age_list] 


# In[32]:


df['old_new'] = old_new


# In[33]:


df.head().old_new


# In[34]:


df.to_csv('../data/used-cars.csv')


# In[ ]:




