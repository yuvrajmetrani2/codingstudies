# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:56:31 2020

@author: Yuvraj
"""
import numpy as np
'''


'''

def w_mean(arr_n, arr_w, arrlength):
    '''
    

    Parameters
    ----------
    arr_n : TYPE - list of numeric values 
        Value array.
    arr_w : TYPE - list of numeric values
        Weight array.
    arrlength : TYPE - numeric value
        length of the lists

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    sum_w = 0
    sum_nw = 0
    for i in range (0,arrlength):
        
        sum_nw +=  int (arr_n[i]) * int ( arr_w[i])
        sum_w += int( arr_w[i])
    
    return ("%.1f" % (sum_nw / sum_w))


length = int(input())
arr_n = (input().split())
arr_w = (input().split())

print(w_mean(arr_n,arr_w,length))




