# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:39:47 2020

https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

problem on binomial distribution

@author: Krishna
"""
'''

The ratio of boys to girls for babies born in Russia is 1.09 : 1.
If there is  child born per birth, what proportion of Russian families 
with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. 
Then print your result, rounded to a scale of 3 decimal places.

# solved answer = 0.696

'''
import math
#family has 6 children
n = 6
#probablilty ratio of boys to girls is 1.09 : 1

#Therefore, p(x) = s / (s+f)

# to find p, q
s = 1.09
f = 1

#odds of s = s/f
#probability P(s) = s/ (1 + s)

#p = s / ( s + f )
#p = s/f

p =  s / ( 1 + s )
q = 1 - p  # q = 1 - p

#print("p = " , p , ", q = ", q)

#Probability Mass Function
#b(x,n,p) = (n/x) * (p**x) * (q **(n-x))

# probability of at least 3 boys out of 6 children
# b(x>=3, n, p) = summation of b(x>=3, n, p)
sumb = 0

def factorial(n):
    return 1 if n == 0 else n * math.factorial(n - 1)

def combination(n, k):
    '''
    to find combination of n of k
    
    '''
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

for x in range (3,7):
    #print(x)
    sumb += combination(n,x) * (p**x) * (q **(n-x))

# Probability of having atleast 3 boys of 6 children
print("%.3f " % sumb)    
    



