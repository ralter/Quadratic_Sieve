:#import numpy as np
from math import ceil,log,sqrt,exp

N=float(input("input a number for factoring: "))
def bounds(N):
    B=ceil((exp(1)**sqrt(log(N)*log(log(N))))**(sqrt(2)/4))
    return B,B**3
B,M=bounds(N)

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
    res=int(a**((p-1)/2)%p)
    if (res==p-1):
        return False
    else:
        return True

