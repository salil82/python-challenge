
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np


# In[39]:


csvpath1 = "budget_data_1.csv"
csvpath1_pd = pd.read_csv(csvpath1)
csvpath1_pd.head()


# In[40]:


csvpath2 = "budget_data_2.csv"
csvpath2_pd = pd.read_csv(csvpath2)
csvpath2_pd.head


# In[41]:


budgets = [csvpath1_pd, csvpath2_pd]


# In[42]:


mergecsv = pd.concat(budgets)
mergecsv.head()


# In[43]:


print("Total Months: " + str(len(mergecsv) + 1))


# In[44]:


revenue = mergecsv['Revenue'].sum()


# In[45]:


print("Total Revenue: $" + str(revenue))


# In[46]:


ave_change = revenue/(len(mergecsv) + 1)


# In[47]:


print ("Average Revenue Change: $" + str(ave_change))


# In[48]:


mergecsv["Difference"] = mergecsv["Revenue"].shift(1) - mergecsv["Revenue"].shift(0)
mergecsv.head


# In[49]:


new_low = mergecsv.sort_values("Difference")

new_low.head


# In[50]:


worst = new_low.iloc[:1]
print("Greatest Decrease in Revenue: " + str(worst))


# In[51]:


new_high = new_low.iloc[::-1]
new_high


# In[52]:


single_high = new_high.iloc[1:2]
single_high


# In[53]:


print("Greatest Increase in Revenue: " + str(single_high))

