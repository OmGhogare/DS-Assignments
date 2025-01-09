#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Data Cleaning and Preparation:


# In[ ]:


import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline 


# In[6]:


df=pd.read_csv(r'C:\Users\OM\Downloads\Cardiotocographic.csv')  # load dataset
df


# In[8]:


df.describe()  # describe dataset


# In[ ]:





# In[9]:


df.isna()  # to check null values if present


# In[10]:


df.head(5)


# In[12]:


df.dtypes   # checking dtypes


# In[14]:


df.info()  # no null value present


# In[21]:


df.boxplot()


# In[ ]:


#outlier detection function


# In[27]:


sns.boxplot(x=df['ASTV'])


# In[28]:


df.columns


# In[33]:


df['ASTV'].quantile(0.75)


# In[32]:


df['ASTV'].quantile(0.25)


# In[34]:


def capping(data,columns):      #outlier removing using capping function
    for col in columns:
        q1=data[col].quantile(0.25)
        q3=data[col].quantile(0.75)
        iqr=q3-q1
        
        lower = q1-(1.5*iqr)
        upper = q3+(1.5*iqr)
        
        df[col] = np.where(df[col] > upper, upper, np.where(df[col] < lower, lower,df[col]))


# In[ ]:





# In[38]:


capping(df,df.drop(columns=['AC']).columns)


# In[39]:


df.boxplot()


# In[ ]:


# 2. Statistical Summary:


# In[40]:


df.describe()


# In[ ]:


'''Several variables like 
 LB, AC, FM, UC, DL, DS, DP, ASTV, MSTV, ALTV, and MLTV, 
contain negative values  which do not make sense depending on the context given
(like:- physiological measurements like fetal heart rates should  be positive).'''


# In[ ]:


# 3. Data Visualization:


# In[45]:


df.boxplot()  # boxplot 
plt.rcParams['figure.figsize']=(10,5)

plt.rcParams['figure.dpi']=150


# In[51]:


sns.pairplot(df)   # pairplot


# In[52]:


sns.heatmap(df.corr(), annot = True, cmap='PiYG')  # 


# In[ ]:


sns.scatterplot(df,'Tendency', 'NSP')


# In[61]:


print(df.columns)


# In[ ]:


#  CONCLUSION
-'''Insights infered from the Exploratory Analysis :-
  1. LB, ASTV, ALTV, MLTV, Width had outliers as infered by Describe function & Boxplot.
  2. LB, AC, DS, DP, Width, Tendency, MLTV, NSP columns had Missing values which were dropped.
  3. The Outliers were replaced by Capping Method (Median).
  4. The Duplicate values present were also dropped as they will have a negative impact on the accuracy of the Final Model.
  5. The Columns [DS, DP & NSP] have no Co-relation with any of the other Columns. 
      They also don't have any kind of relation with each other which is strange
  6. At first, the Histogram plotted did not have any Normal Distribution, but after replacing the Outliers they had a Normal Distribution.
  
  '''

