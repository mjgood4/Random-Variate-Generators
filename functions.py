
def prn_generator(num_vars=50000,seed=52545):
    random_list=[]
    x=seed
    for i in range(0,num_vars):
        x=(16807*x)%(2**31-1)
        random_list.append(x/(2**31-1))
    return random_list


def bern_generator(p,num_vars=50000,seed=52545):
    bernoulli_list = []
    for i in prn_generator(num_vars,seed):
        if i<(1-p):
            bernoulli_list.append(0)
        else:
            bernoulli_list.append(1)
    return bernoulli_list


def geom_generator(p,num_vars=50000,seed=52545):
    from math import ceil
    from numpy import log
    geometric_list=[]
    for i in prn_generator(num_vars,seed):
        geometric_list.append(ceil(log(i)/log(1-p)))
    return geometric_list


def exp_generator(lam,num_vars=50000,seed=52545):
    from math import log
    exp_list=[]
    for i in prn_generator(num_vars,seed):
        exp_list.append((-1/lam)*log(1-i))
    return exp_list

def norm_generator(mu,sig_sq,num_vars=50000,seed=52545):
    normal_list=[]
    for i in prn_generator(num_vars,seed):
        normal_list.append(mu + (sig_sq**.5)*(i**.135-(1-i)**.135)/.1975)
    return normal_list


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


def weibull_generator(alpha,beta,num_vars=50000,seed=52545):
    from math import log
    weibull_list=[]
    for i in prn_generator(num_vars,seed):
        weibull_list.append((1/alpha)*(-log(1-i))**(1/beta))
    return weibull_list

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
            

def triangular_generator(num_vars,seed1=52545,seed2=3079):
    unif_list1=prn_generator(num_vars,seed1)
    unif_list2=prn_generator(num_vars,seed2)
    return [sum(x) for x in zip(unif_list1, unif_list2)]


def negbin_generator(n,p,num_vars=50000,seed=52545):
    negbin=[]
    for i in range(0,num_vars):
        result=0
        for j in geom_generator(1-p,n,seed):
            result+=j
            seed+=1
        negbin.append(result)
    return negbin

