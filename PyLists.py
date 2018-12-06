# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:13:26 2018

@author: kmuthu2
"""

list1 = [1,23,4,'hi','hello',[2334,56,7678,78]]

list1[2]

list1[-1][0]

list1.index('hi')

len(list1)


tuple1 = (1,2,3,4)
list2 = [1,23,4,'hi','hello',[2334,56,7678,78],tuple1]

list1 += tuple1

check = bool(list1 == list2) 

#Check value not true

list1.append(tuple1)
check1 = bool(list1 == list2)
#True 

'''
Just by + tuple elements are added but only as separate elements so false comes
 for check

but in check1 we used the append function of the list so it appends 
'''

del list1[1]

list1.remove('hello')

list1.pop(0)
#Aliasing in python
x = ['A','B','C']
y = x







