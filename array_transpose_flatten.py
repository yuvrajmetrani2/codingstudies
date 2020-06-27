# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:53:53 2020

@author: Krishna

Sample Input

2 2
1 2
3 4


Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]
"""

import numpy

n, m =  map(int,input().split()) 
inarray = numpy.array([input().strip().split() for _ in range(n)], int)

print(inarray.T)
print(inarray.flatten())
'''
'''