#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset = pd.read_csv("Ecommerce Purchases")


# In[3]:


dataset


# In[4]:


dataset.head()


# In[5]:


dataset.tail()


# In[6]:


dataset.head(10)


# In[7]:


dataset.tail(10)


# In[11]:


dataset["CC Security Code"].dtypes


# In[13]:


dataset.isnull().sum()


# In[14]:


len(dataset)  ## no. of rows


# In[15]:


len(dataset.columns)


# In[16]:


dataset.shape


# In[17]:


dataset.info


# In[18]:


dataset["Purchase Price"].max()  ##Check the Highest "Purchase Price" in the DataSet


# In[19]:


dataset[["Purchase Price","Email"]].min()  ## Display the Lowest "Purchase Price" in the DataSet


# In[20]:


dataset["Purchase Price"].mean() ##What is the Average Purchase Price so far?


# In[21]:


len(dataset[dataset["Language"]=="fr"])   # How many customers have French as their primary language?


# In[22]:


len(dataset[dataset["Job"].str.contains('engineer',case=False)])  #What is the Email address of the person having IP Address: 24.140.33.94


# In[23]:


dataset[dataset["IP Address"]=="24.140.33.94"]['Email']   ## How many of our customers are any kind of Engineer?


# In[24]:


len(dataset[(dataset["CC Provider"]=="Mastercard") & (dataset["Purchase Price"]>50)])  #How many people have Mastercard as thier credit card provider and made a purchase above 50?


# In[25]:


#How many people use credit cards during the Morning time?
len(dataset[dataset['AM or PM']=="AM"])


# In[27]:


len(dataset[dataset['AM or PM']=="PM"])
#How many people use credit cards during the night time?


# In[28]:


##Number of people that are having a credit card that will expire in 2020. Also find their Email
dataset[dataset["CC Exp Date"].apply(lambda x: x[3:]=="20")]['Email'].head()


# In[29]:


## Show the Top 5 email providers
dataset["Email"].apply(lambda x: x.split('@')[1]).value_counts().head()


# In[30]:


#  Print the Top 5 companies having the highest purchase prices
dataset[['Company','Purchase Price']].nlargest(5,'Purchase Price').head()


# In[ ]:




