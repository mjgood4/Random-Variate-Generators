#!/usr/bin/env python
# coding: utf-8

# In[1]:


import functions as fn


# <h5>Generate a list of 10 PRNs

# In[2]:


fn.prn_generator(10)


# <h5>I drink coke 1 out of every 10 days. Simulate 100 days to predict on how many I will drink coke.

# In[3]:


elements=fn.bern_generator(.1,100)
sum(map(lambda x : x==1, elements))


# <h5>Using the probability from the last question, determine how many days it will take for me to drink a coke

# In[4]:


fn.geom_generator(.1,1)


# <h5>Let's say I drink coke 7 out of 10 days. Find the average number of days I drink coke before the third day I don't drink a coke from 200 trials.

# In[5]:


import statistics
statistics.mean(fn.negbin_generator(3,.7,200))


# <h5>Given lambda equals .02, tell me the interarrival times of the first 5 customers to the barbershop

# In[6]:


fn.exp_generator(.02,5)


# Tell me the average number of customers expected to arrive at the barbershop within the first hour from 100 trials.

# In[7]:


statistics.mean(fn.poisson_generator(.02,60,100))


# <h5> How many standard deviations is the 5th normal random variate away from the mean when mu=10 and variance=100?

# In[8]:


fn.norm_generator(10,10,5)[4]/10


# <h5>We don't know much about the distribution of a barber's service time, but we do know that he takes an average of 10 minutes to cut hair with a min of 5 and a max of 15. Use a triangular distribution to generate his first customer's service time.

# In[9]:


fn.triangular_generator(1)[0]*10+5


# <h5>Give the average random variate value generated from a gamma distribution with alpha=10 and beta=1000 for 100 trials

# In[10]:


statistics.mean(fn.gamma_generator(10,1000,100))


# <h5>Give the expected life of a product generated from a weibull distribution with alpha=10 and beta=1000 for 100 trials

# In[11]:


statistics.mean(fn.weibull_generator(10,1000,100))

