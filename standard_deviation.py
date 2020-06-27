# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:24:55 2020

Standard Deviation

@author: Yuvraj

"""
'''
5
10 40 30 50 20

Could use the statistics module, but just tried it for a Hackerrank piece.
'''
#import statistics as sts
n= int(input())
x = list(map(float, input().split()))

mean = sum(x)/n
sqr_mean_distance = []

for i in range (0,n):
    sqr_mean_distance.append((x[i] - mean)**2)

print((sum(sqr_mean_distance)/n) ** (1/2))
