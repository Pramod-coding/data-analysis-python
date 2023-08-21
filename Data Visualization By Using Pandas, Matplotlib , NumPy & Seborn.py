#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# In[1]:


import numpy as np# For Multi dimensional arrays
import pandas as pd# For DataFraems
import matplotlib.pyplot as plt# For Data Visualizations
import seaborn as sns# for Advance Visualizations
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# In[97]:


#Importing external File to Pyhon Environment
rw=pd.read_csv(r"D:\DS\Practice\Raw Data\data.csv")
rw


# In[3]:


len(rw)# Gives the length of the Dataset no.of Rows


# In[4]:


rw.info()# Gives the Total Information about the Ds


# In[5]:


rw.shape# Gives total No.of   Rows & Columns


# In[6]:


rw.columns# Gives Names of the columns


# In[7]:


rw.head()# Default Gives Top 5 Rows


# In[8]:


rw.head(20)# Gives Top 20 Rows 


# In[9]:


rw.tail()# Default Gives Bottom 5 rows


# In[10]:


rw.tail(15)# Gives bottom 15 rows


# In[11]:


type(rw)# DAta type of the Rw Dataset


# # Descriptive Analysis:
# #Gives the descriptive (stastical) info of Numirical Dat only

# In[12]:


rw.describe()


# In[13]:


rw.count()


# In[14]:


rw.std()# It quantifies how much the individual values in a dataset differ from the mean (average) value.


# In[15]:


rw.min()# It Gives the Minimum value info of neumarical data


# In[16]:


rw.quantile(0.25) # Gives 25% of the neumarical data


# In[17]:


rw.quantile(0.5) # Gives 50% of the neumarical data


# In[18]:


rw.quantile(0.75) # Gives 75% of the neumarical data


# In[19]:


rw.max() # Gives the Max Values Of the Rw Dataset


# In[20]:


rw.describe().transpose()# Converts all rows to columns


# # INDEXING/SLICING:
# 

# In[21]:


rw[:]


# In[22]:


rw[:8]


# In[23]:


rw[190:]


# In[24]:


#Reverse Slicing 
rw[::-1]


# In[25]:


rw[::6]# Step Indexing


# In[26]:


rw[0:200:20]# Slicing for every 20th row


# In[27]:


rw[100:120][['CountryName','BirthRate']]# Slicing of individual vaiables


# In[28]:


rw[['CountryName','InternetUsers']][190:198]


# # Spliting the data

# In[29]:


rwN=rw.select_dtypes(include='number')# Spliting Of Neumarical attributes from A DataFrame
rwN


# In[30]:


rwC=rw.select_dtypes(include='object')# Spliting Of Categorical  attributes from A DataFrame
rwC


# In[31]:


# Mathematical operations:


# In[32]:


rw[:]


# In[33]:


rw.BirthRate * rw.InternetUsers


# In[34]:


rw.BirthRate / rw.InternetUsers


# In[35]:


rw['Multp']=rw.BirthRate * rw.InternetUsers # Adding a Attribute
rw


# In[36]:


rw=rw.drop('Multp', axis=1)# For Dropping a variable from a Dataset axis=1 is Used for Column,
                           # axis=0 is used to drop a Row.
rw[:]


# In[37]:


#Conditional categorization


# In[38]:


br=rw.BirthRate <20
len(rw[br])


# In[39]:


it=rw.InternetUsers > 20
len(rw[it])


# In[40]:


[br & it]


# In[41]:


rw[br & it]


# In[42]:


rw[(rw.BirthRate>29)&(rw.InternetUsers < 30)]


# In[44]:


rw.IncomeGroup.unique() # To Get all the Unique values in the attribute


# ![image.png](attachment:image.png)
# 
# # For Advance Visualization
# 

# In[45]:


#Seaborn is a powerful Python data visualization library built on top of Matplotlib.
#It provides a high-level interface for creating attractive and informative statistical graphics.
#Seaborn is especially useful for visualizing complex datasets with minimal code and is widely used in 
#data analysis and exploration tasks.


# In[48]:


#1.Scatter Plot (sns.scatterplot()):
#A scatter plot displays the relationship between two continuous variables by representing each data point
#as a dot on the plot.

#2.Line Plot (sns.lineplot()):
#Line plots are used to visualize the trend of a continuous variable over time or other continuous
#dimensions.

#3.Bar Plot (sns.barplot()):
#A bar plot displays categorical data with rectangular bars, representing the count or mean of the data
#for each category.

#4.Count Plot (sns.countplot()):
#A count plot is a specialized form of a bar plot used to show the counts of observations in each category.

#5.Histogram (sns.histplot()):(displot)
#Histograms display the distribution of a single variable by dividing the data into bins and showing the 
#frequency of data points within each bin.

#6.Box Plot (sns.boxplot()):
#A box plot (box-and-whisker plot) displays the distribution of data across quartiles, showing the median,
#interquartile range, and outliers.

#7.Violin Plot (sns.violinplot()):
#A violin plot combines a box plot with a kernel density plot to display the distribution of data across 
#different categories.

#8.Heatmap (sns.heatmap()):
#A heatmap displays the correlation between variables using a color-coded matrix.

#9.Pair Plot (sns.pairplot()):
#A pair plot creates a grid of scatter plots, useful for exploring relationships between multiple variables
#in a dataset.

#10.Joint Plot (sns.jointplot()):
#A joint plot displays the relationship between two variables along with their individual distributions.

#11.Facet Grid (sns.FacetGrid()):
#Facet grids allow you to create multiple plots arranged in rows and columns based on the values of
#one or more categorical variables.

#12.lmplot (sns.lmplot()):
#An lmplot creates scatter plots with regression lines, which are useful for exploring linear
#relationships between variables.
    


# In[58]:


#1.Scatter Plot (sns.scatterplot()):
#A scatter plot displays the relationship between two continuous variables by representing each data point
#as a dot on the plot.

rw1=sns.scatterplot(data=rw, x='IncomeGroup', y='BirthRate')


# In[61]:


#2.Line Plot (sns.lineplot()):
#Line plots are used to visualize the trend of a continuous variable over time or other continuous
#dimensions.
rw2=sns.lineplot(data=rw, x='IncomeGroup', y='BirthRate')


# In[65]:


#3.Bar Plot (sns.barplot()):
#A bar plot displays categorical data with rectangular bars, representing the count or mean of the data
#for each category.
rw3=sns.barplot(data=rw, x='IncomeGroup', y='BirthRate')


# In[66]:


#4.Count Plot (sns.countplot()):
#A count plot is a specialized form of a bar plot used to show the counts of observations in each category.

rw4=sns.countplot( x='IncomeGroup',data=rw )


# In[67]:


#5.Histogram (sns.histplot()):(displot)
#Histograms display the distribution of a single variable by dividing the data into bins and showing the 
#frequency of data points within each bin.
rw5=sns.histplot(data=rw, x='IncomeGroup', y='BirthRate')


# In[71]:


rw5_A=sns.displot(data=rw, x='IncomeGroup', y='BirthRate')


# In[70]:


#6.Box Plot (sns.boxplot()):
#A box plot (box-and-whisker plot) displays the distribution of data across quartiles, showing the median,
#interquartile range, and outliers.

rw6=sns.boxplot(data=rw, x='IncomeGroup', y='BirthRate')


# In[72]:


#7.Violin Plot (sns.violinplot()):
#A violin plot combines a box plot with a kernel density plot to display the distribution of data across 
#different categories.

rw7=sns.violinplot(data=rw, x='IncomeGroup', y='BirthRate')


# In[85]:


##8.Heatmap (sns.heatmap()):
#A heatmap displays the correlation between variables using a color-coded matrix.

rw_cr=rw[0:12]
rw_pd = pd.crosstab(index=rw_cr['CountryName'], columns=rw_cr['IncomeGroup'])

rw8=sns.heatmap(rw_pd, annot=True, cmap='Blues', fmt='d')


# In[94]:


#9.Pair Plot (sns.pairplot()):
#A pair plot creates a grid of scatter plots, useful for exploring relationships between multiple variables
#in a dataset.
rw9=sns.pairplot(rw)


# In[95]:


#10.Joint Plot (sns.jointplot()):
#A joint plot displays the relationship between two variables along with their individual distributions.
rw10=sns.jointplot(rw)


# In[104]:


#11.Facet Grid (sns.FacetGrid()):
#Facet grids allow you to create multiple plots arranged in rows and columns based on the values of
#one or more categorical variables.
rwF = sns.FacetGrid(rw, col='IncomeGroup')
rwF.map(sns.scatterplot, 'BirthRate', 'InternetUsers')


# In[105]:


#12.lmplot (sns.lmplot()):
#An lmplot creates scatter plots with regression lines, which are useful for exploring linear
#relationships between variables.
rw12=sns.lmplot(x='BirthRate', y='InternetUsers', hue='IncomeGroup', data=rw, markers="o")


# In[ ]:




