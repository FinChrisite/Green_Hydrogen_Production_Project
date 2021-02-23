#!/usr/bin/env python
# coding: utf-8

# In[19]:


import calliope


# In[20]:


model = calliope.Model('C:/UniPython/Green_Hydrogen_Production_Project/poc_Model/model.yaml')
model.run()


# In[21]:


model.plot.timeseries(array=['electricity', 'resource_prod'])


# In[22]:


model.plot.timeseries(array=['hydrogen', 'resource_prod'])


# In[23]:


model.plot.summary(to_file= '/UniPython/Green_Hydrogen_Production_Project/poc_results_file2.html')


# In[ ]:




