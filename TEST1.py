#!/usr/bin/env python
# coding: utf-8

# QUES 1

# In[3]:


sampledict={
    'country':{
        'indian cricket team':{
            'name':['rohit','virat','rahul','shami','bumrah'],
            'runs':{
                'rohit':47,
                'virat':54,
                'rahul':66
            }
        }
    }
}


# In[113]:


virat_runs = sampledict['country']['indian cricket team']['runs']['virat']
print(virat_runs) 


# In[98]:


value=sampledict.values()


# In[99]:


value


# In[102]:


if 'virat' in value:
    print("virat : 54")


# QUES 2

# In[26]:


sample_dict={'a':100,'b':2800,'c':300}


# In[31]:


nlist=list(sample_dict.items())


# In[32]:


if 2800 in nlist:
    print('yes it is present')

else:
    print('no 2800 does not exist in the dict')


# QUES 3

# In[33]:


sample_set={'surya','kapil','msd'}
sample_list=['sachin','siraj','sehwag']


# In[34]:


sample_set.update(sample_list)


# In[37]:


sample_set


# QUES 4

# In[105]:


set1={10,20,30,40,50}
set2={30,40,50,60,70}


# In[107]:


for i in set2:
    print(i,'\n')


# In[109]:


nset=set()
for i in set1:
    for j in set2:
        if i==j:
            nset.add(i)


# In[110]:


nset


# QUES 5

# In[43]:


numbers=[1,2,3,4,5,6,7]


# In[44]:


sqrs=[]
for i in numbers:
    i=i**2
    sqrs.append(i)


# In[45]:


sqrs


# QUES 6

# In[53]:


list=[10,20,[300,400,[5000,6000],500],30,40]


# In[55]:


list


# In[57]:


lis=list[2][2]


# In[58]:


lis.append(7000)


# In[59]:


list


# In[ ]:




