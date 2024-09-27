#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Machine learning is like teaching a computer to learn from examples and make decisions or predictions based on what it has learned 
# using the data provided or the data over which the model has been trained.


# for example objects like cat & dog 


# In[52]:


# The URL of the file
url = 'https://raw.githubusercontent.com/jakevdp/marathon-data/master/marathon-data.csv'

# Use the ! symbol to run a shell command in Jupyter
get_ipython().system('curl -o marathon-data.csv {url}')


# In[53]:


import pandas as pd
a=pd.read_csv('usahousing.csv')
a.iloc[:,:]


# In[54]:


import seaborn as sns
sns.get_methods


# In[55]:


import seaborn as sns
sns.pairplot(a)


# In[56]:


sns.displot(a['Price'])


# In[57]:


a.isnull().sum()


# In[58]:


a.describe()


# In[59]:


a.info()


# In[60]:


sns.heatmap(a.corr(numeric_only=True))


# In[61]:


#Training a Linear Regression Model -
a.head()


# In[62]:


a.columns


# In[63]:


X=a[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
y=a['Price']


# In[64]:


a.shape


# In[65]:


# 5000=60% will be used for training and 40% will be used for testing 


# In[66]:


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)


# In[67]:


X_train.shape


# In[68]:


from sklearn.linear_model import LinearRegression
lm=LinearRegression()


# In[69]:


lm.fit(X_train,y_train)


# In[70]:


pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])


# In[ ]:


import matplotlib.pyplot as mt

b=list(a['Avg. Area Income'])
c=list(a['Area Population'])

mt.plot(b,c,marker='*')


# In[ ]:


help()


# In[ ]:


get_ipython().run_line_magic('pinfo', 'sklearn.neural_network')


# In[ ]:


def func(a,b):
    return b if a==0 else func(b%a,a)

print(func(30,75))


# In[ ]:


numbers=(4,7,19,2,89,45,72,22)
sorted_numbers=sorted(numbers)
even=lambda:a%2==0
even_numbers=filter(even,sorted_numbers)
print(type(even_numbers))


# In[15]:


even_numbers=filter(even,sorted_numbers)
print(even_numbers)


# In[16]:


print(4**3+(7+5)**(1+1))


# In[17]:


64+144


# In[33]:


captains={}
captains


# In[43]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
 "Discovery": "unknown"
}
for ship,captain in captains.items():
    print(f"The {ship} is captained by {captain}.")


# In[74]:


17//3


# In[ ]:


prompt='hey whatsup'
user_input=input(prompt)
print('you sais',+user_input)


# In[ ]:




