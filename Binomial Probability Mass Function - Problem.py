# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:39:47 2020

https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

problem on binomial distribution

@author: Krishna
"""
'''

A manufacturer of metal pistons finds that, on average, 
12% of the pistons they manufacture are rejected because they are 
incorrectly sized. 
What is the probability that a batch of 10 pistons will contain:

1. No more than 2 rejects?
2. At least 2 rejects?

Input (stdin)
12 10

Expected Output (solved)

0.891
0.342
'''
from math import factorial

p = 12/100.0
q = 1-p

N = 10

B0 = factorial(N)/(factorial(0)*factorial(N-0)) * p**0 * q**(N-0)
B1 = factorial(N)/(factorial(1)*factorial(N-1)) * p**1 * q**(N-1)
B2 = factorial(N)/(factorial(2)*factorial(N-2)) * p**2 * q**(N-2)

print(round(B0+B1+B2,3))
print(round(1-(B0+B1),3))