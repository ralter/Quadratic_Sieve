import numpy as np
from math import ceil,log,sqrt,exp
from scipy.linalg import null_space

def bounds(N):
    B=ceil((exp(1)**sqrt(log(N)*log(log(N))))**(sqrt(2)/4))
    return 7*B,B**3

def gcd(a,b):
    r=a%b
    while r:
        a=b
        b=r
        r=a%b
        print(a,b)
    return b

def sieve_of_eratosthenes(val):
    tot = val+1
    lst = [True] * tot 
    for i in range(2, int(val**0.5 + 1)):
        if lst[i]:
            for j in range(i*i,tot, i):
                lst[j] = False
    final = []
    for i in range(2, tot):
        if lst[i]:
            final.append(i)
    return final

def prime_factors(y):
    i = 2
    factors = []
    while i * i <= y:
        if y % i:
            i += 1
        else:
            y //= i
            factors.append(i)
    if y > 1:
        factors.append(y)
    return factors

def eulers_criterion(a,p):
    res=pow(a, (p-1)//2, p)
    if (res==p-1):
        return False
    elif (res==1):
        return True

def eulers_criterion_loop(a,primes):
    kept = []
    for p in primes:
        if eulers_criterion(a,p):
            kept.append(p)
    return kept

def gen_primes(b,n):
    base = sieve_of_eratosthenes(b)
    better = eulers_criterion_loop(n,base)
    return better

def keep_to_mat(keep,primes):
    mat = np.zeros((len(keep),len(primes)),int)
    for i in range (len(keep)):
        el = keep[i]
        for num in el[0]:
            mat[i][primes.index(num)] = ((mat[i][primes.index(num)])+1)%2 
    return mat  

def factorable_nums(N,m,fac_base):
    keep=[]
    for x in range(m+1):
        check=prime_factors((pow(x+ceil(sqrt(N)),2)-N)%N)  
        if set(check).issubset(fac_base):
            keep.append([check,(pow(x+ceil(sqrt(N)),2)-N)%N])
    return keep

def N_to_matrix(N):
    B,m=bounds(N)
    fac_base=gen_primes(B,N)
    print(fac_base)
    keep=factorable_nums(N,m,fac_base)
    mat=keep_to_mat(keep,fac_base)
    return mat


### Actual Script!!!

N=int(input("input a number for factoring: "))
mat=N_to_matrix(N)
print(mat.shape)
print(mat)
ns = null_space(mat)
ns=np.array(ns,dtype=int)
print(ns)
