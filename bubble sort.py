# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:36:49 2020

@author: Krishna
"""

def bubble_sort(arr, increasing = True):
    '''
    

    Parameters
    ----------
    arr : List
        List of numeric values.
    increasing : Bool, optional
        Sorting increasing or decreasing. The default is True.

    Returns
    -------
    arr : TYPE list 
        DESCRIPTION - Sorted array.
    itercount : integer
        DESCRIPTION - The number of cycles of loop the algorithm took to sort..

    '''
    
    itercount = 0
    while True:
        corrected  = False
        for i in range(0, len(arr)-1):
            #check for each pair of array items
            if(increasing):
                if (arr[i] > arr[i+1]):
                    arr[i],arr[i+1] = arr[i+1], arr[i]
                    corrected = True 
                
            else:
                if (arr[i] < arr[i+1]):
                    arr[i],arr[i+1] = arr[i+1], arr[i]
                    corrected = True
            if corrected:
                itercount +=1
       
        if not corrected:
            return arr, itercount

def swap_arrayitems(a,b):
    a,b = b,a
    return a,b

sortedarry , iterations =  (bubble_sort([8,2,3,4,5,6]))

print(iterations, " -> " , sortedarry)

print (bubble_sort([9,3,0,6,-4,5,1], True))
#print (bubble_sort([a, z, g,b,c,e,o,f]))
print(bubble_sort([2,4,1]))
print(bubble_sort([2,4,1],False))

