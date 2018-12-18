# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 17:10:25 2018

@author: KarthikM
"""

import numpy as np

x = np.array([1,2,3])

print(x.dtype)

x = np.array([1,2,3.0])
print(x.dtype)


x = np.array([1,2,3,4,5],ndmin=2)
print(x.shape)


x = np.array([1,2,3,4,5],ndmin=3)
print(x.shape)


x= np.arange(10)
s = slice(3,9,2)
print(x[s])

print(x[3:9:1])

print(x[:7])

print(x[3:])  # from 3 to last

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)

print(x[1:])  # row of index 1 and 2 will be printed

# To print column 

print(x[:,1]) #print 1st column 

x = [1,2,3]
y = [4,5,6]
print(x+y)

#numpy

    x = np.array([1,2,3])
    y = np.array([4,5,6])
    print(x+y)


x = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.mean(x))
print(np.min(x))
print(np.max(x))
print(np.var(x))
print(np.std(x))
print(np.argmax(x))
print(np.argmin(x))

print(np.where(x>3))
condition = (x>3) & (x<9)
print(np.extract(condition,x))







































