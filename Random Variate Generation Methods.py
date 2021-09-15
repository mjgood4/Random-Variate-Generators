#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


#create a list of PRNs for use with the "desert island" generator
def prn_generator(num_vars=50000,seed=52545):
    random_list=[]
    x=seed
    for i in range(0,num_vars):
        x=(16807*x)%(2**31-1)
        random_list.append(x/(2**31-1))
    return random_list

sns.distplot(prn_generator())


# In[3]:


#Bernoulli - if our PRN is less than 1-p, set the bernoulli trial equal to 0
def bern_generator(p,num_vars=50000,seed=52545):
    bernoulli_list = []
    for i in prn_generator(num_vars,seed):
        if i<(1-p):
            bernoulli_list.append(0)
        else:
            bernoulli_list.append(1)
    return bernoulli_list

sns.distplot(bern_generator(.4))


# In[4]:


#Geometric - use Inverse Trans Method formula derived in class
def geom_generator(p,num_vars=50000,seed=52545):
    from math import ceil
    from numpy import log
    geometric_list=[]
    for i in prn_generator(num_vars,seed):
        geometric_list.append(ceil(log(i)/log(1-p)))
    return geometric_list

sns.distplot(geom_generator(.4))


# In[5]:


#Exponential - use inverse trans method formula derived in class
def exp_generator(lam,num_vars=50000,seed=52545):
    from math import log
    exp_list=[]
    for i in prn_generator(num_vars,seed):
        exp_list.append((-1/lam)*log(1-i))
    return exp_list

sns.distplot(exp_generator(5))


# In[6]:


#Normal using BCNN approximation for Z
def norm_generator(mu,sig_sq,num_vars=50000,seed=52545):
    normal_list=[]
    for i in prn_generator(num_vars,seed):
        normal_list.append(mu + (sig_sq**.5)*(i**.135-(1-i)**.135)/.1975)
    return normal_list

sns.distplot(norm_generator(5,10))


# In[7]:


#Gamma - I got help from https://www.cs.toronto.edu/~radford/csc2541.F04/gamma.html for a method to generate from uniform
#Generate uniforms within the method
def gamma_generator(alpha,beta,num_vars=50000,seed=52545):
    from math import log
    gamma_list=[]
    x=seed
    for i in range(0,num_vars):
        l_list=[]
        for i in range(0,alpha):
            x=(16807*x)%(2**31-1)
            l_list.append(-1*log(1-x/(2**31-1)))

        S=sum(l_list)

        gamma_list.append(S/beta)

    return gamma_list

sns.distplot(gamma_generator(10,1000))


# In[8]:


#weibull - use inverse trans method derived in class
def weibull_generator(alpha,beta,num_vars=50000,seed=52545):
    from math import log
    weibull_list=[]
    for i in prn_generator(num_vars,seed):
        weibull_list.append((1/alpha)*(-log(1-i))**(1/beta))
    return weibull_list

sns.distplot(weibull_generator(5,1))


# In[9]:


#poisson - for each step, calculate the CDF and check if the PRN is less than that step's cdf
def poisson_generator(lam,time_int=1,num_vars=50000,seed=52545):
    from math import exp, factorial
    lam=lam*time_int
    poisson_list=[]
    for i in prn_generator(num_vars,seed):
        cdf=0
        x=-1
        while i>cdf:
            x+=1
            cdf+=(exp(-lam)*lam**x)/factorial(x)
        poisson_list.append(x)
    return poisson_list
            
sns.distplot(poisson_generator(5))    


# In[10]:


#triangular - add two uniforms
def triangular_generator(num_vars,seed1=52545,seed2=3079):
    unif_list1=prn_generator(num_vars,seed1)
    unif_list2=prn_generator(num_vars,seed2)
    return [sum(x) for x in zip(unif_list1, unif_list2)]

sns.distplot(triangular_generator(50000))


# In[11]:


#negative binomial - add n geometrics, change seed for each iteration
def negbin_generator(n,p,num_vars=50000,seed=52545):
    negbin=[]
    for i in range(0,num_vars):
        result=0
        for j in geom_generator(p,n,seed):
            result+=j
            seed+=1
        negbin.append(result)
    return negbin

sns.distplot(negbin_generator(10,.5))

