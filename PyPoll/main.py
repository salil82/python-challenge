
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


csvpath1 = "election_data_1.csv"
csvpath1_pd = pd.read_csv(csvpath1)
csvpath1_pd.head()


# In[6]:


csvpath2 = "election_data_2.csv"
csvpath2_pd = pd.read_csv(csvpath2)


# In[7]:


elections = [csvpath1_pd, csvpath2_pd]


# In[9]:


mergecsv = pd.concat(elections)
mergecsv.head


# In[23]:


print("Total Votes: " + str(len(mergecsv) + 1))


# In[29]:


candidate = mergecsv.Candidate.unique()
print("Candidate: "+ candidate)


# In[37]:


Vestal = mergecsv.Candidate.value_counts()["Vestal"]
print("Vestal " + str(Vestal) + " votes")
Torres = mergecsv.Candidate.value_counts()["Torres"]
print("Torres " + str(Torres) + " votes")
Seth = mergecsv.Candidate.value_counts()["Seth"]
print("Seth " + str(Seth) + " votes")
Cordin = mergecsv.Candidate.value_counts()["Cordin"]
print("Cordin " + str(Cordin) + " votes")
Khan = mergecsv.Candidate.value_counts()["Khan"]
print("Khan " + str(Khan) + " votes")
Correy = mergecsv.Candidate.value_counts()["Correy"]
print("Correy " + str(Correy) + " votes")
Li = mergecsv.Candidate.value_counts()["Li"]
print("Li " + str(Li) + " votes")


# In[38]:


print("Winner of the popular vote: Khan")

