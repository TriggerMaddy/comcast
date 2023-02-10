#!/usr/bin/env python
# coding: utf-8

# # Comcast Telecom Consumer Complaints

# ### Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\\Users\\SONY\\Downloads\\1568699544_comcast_telecom_complaints_data (2)\\Comcast_telecom_complaints_data.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.isnull().sum()


# # There are no Nan values present in the dataset

# In[6]:


df.describe(include='all')


# In[7]:


df.shape


# In[8]:


df.size


# In[9]:


df=df.drop(['Ticket #','Time'],axis=1)


# In[10]:


df.head()


# In[11]:


#Pandas to_datetime() method to convert string Date time into python date time object.
df['Date_month_year']=df['Date_month_year'].apply(pd.to_datetime)
#setting 'Date_month_year' as index
df=df.set_index('Date_month_year')


# # plotting monthly chart

# In[12]:


#dataframe.groupby()function is splitting the data into groups according to frequency
monthly=df.groupby(pd.Grouper(freq='M')).size().plot()
plt.xlabel('MONTHS')
plt.ylabel('FREQUENCY')
plt.title('MONTHLY TREND CHART')


# #INSIGHT:- From the above trend chart, we can clearly see that complaints for the month of june 2015 are maximum

# In[13]:


#value count() function is getting a series containing counts of unique values for date column.
df['Date'].value_counts(dropna=False)[:8]


# # plotting daily chart

# In[14]:


df=df.sort_values(by='Date')
plt.figure(figsize=(6,6))
df['Date'].value_counts().plot()
plt.xlabel('MONTHS')
plt.ylabel('FREQUENCY')
plt.title('Daily TREND CHART')


# ## Task-2 provide a table with the frequency of complaints types

# In[15]:


df['Customer Complaint'].value_counts(dropna=False)[:9]


# In[16]:


df['Customer Complaint'].value_counts(dropna=False)[:9].plot.bar()


# # Task-3 Which complaint types are maximum i.e.,around internet, network issue, or across any other domains.

# In[17]:


internet_issues1=df[df['Customer Complaint'].str.contains('network')].count()


# In[18]:


internet_issues2=df[df['Customer Complaint'].str.contains('speed')].count()


# In[19]:


internet_issues3=df[df['Customer Complaint'].str.contains('data')].count()


# In[20]:


internet_issues4=df[df['Customer Complaint'].str.contains('internet')].count()


# In[21]:


billing_issues1=df[df['Customer Complaint'].str.contains('bill')].count()


# In[22]:


billing_issues2=df[df['Customer Complaint'].str.contains('billing')].count()


# In[23]:


billing_issues3=df[df['Customer Complaint'].str.contains('charges')].count()


# In[24]:


service_issues1=df[df['Customer Complaint'].str.contains('service')].count()


# In[25]:


service_issues2=df[df['Customer Complaint'].str.contains('customer')].count()


# In[26]:


total_internet_issues=internet_issues1+internet_issues2+internet_issues3+internet_issues4
print(total_internet_issues)


# In[27]:


total_billing_issues=billing_issues1+billing_issues2+billing_issues3
print(total_billing_issues)


# In[28]:


total_service_issues=service_issues1+service_issues2
print(total_service_issues)

# INSIGHT:- From the above analysis we can see that the other issues are maximum.
# # 4. Create a new categorical variable with values as Open and Closed. Open and Pending is to be categorized as Open and Closed $ Solved is to be categorized as Closed

# In[29]:


df.Status.unique()


# In[31]:


df['new_Status']=['Open' if Status=='Open' or Status=='Pending' else 'Closed' for Status in df['Status']]
df=df.drop(['Status'],axis=1)
df


# # Which state has the maximum complaints

# In[32]:


df.groupby(['State']).size().sort_values(ascending=False)[:5]


# # INSIGHTS:-From the above table, we can clearly see that Georgia has maximum complaints.

# In[ ]:





# # Task-6 Provide stats wise status of complaints in a stacked bar chart.

# In[35]:


Status_complaints=df.groupby(['State','new_Status']).size().unstack()
print(Status_complaints)


# In[36]:


Status_complaints.plot.bar(figsize=(10,10),stacked=True)


# INSIGHT:- From the above chart, we can clearly see that Georgia has maximum complaints

# # Task-7 State which has the highest percentage of unsolved complaints

# In[37]:


print(df['new_Status'].value_counts())


# In[38]:


unresolved_data=df.groupby(['State','new_Status']).size().unstack().fillna(0).sort_values(by='Open',ascending=False)
unresolved_data['Unresolved_cmp_prct']=unresolved_data['Open']/unresolved_data['Open'].sum()*100
print(unresolved_data)
unresolved_data.plot()


# # INSIGHTS:- From the table generted above we can see that georgia has maximum unresolved complaints i.e 80

# # Task-8 Provide the percentage of complaints resolved till date, which were received through the internet and customer care calls

# In[ ]:





# In[42]:


resolved_data=df.groupby(['Received Via','new_Status']).size().unstack().fillna(0)
resolved_data['resolved']=resolved_data['Closed']/resolved_data['Closed'].sum()*100
resolved_data['resolved']


# In[46]:


resolved_data.plot(kind='bar',figsize=(8,8))


# In[ ]:




