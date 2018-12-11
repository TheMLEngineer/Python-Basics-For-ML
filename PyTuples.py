# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:45:31 2018

@author: kmuthu2
"""

#Creating tuples

tuple1 = ('Vanakkam')
print(type(tuple1)) 
'''
But the printed type is string ... 

To overcome this
'''
tuple2 = ('Vanakkam',)
print(type(tuple2))

mytuple = ('india','US','UK','Canada','Australia')

mytuple[0]

#Tuple concatenation 

concattuple = ('IT','Programming')
mytuple += concattuple

tuplenesting = (concattuple,tuple2)

#deleting tuples 

del tuple2
print('tuple repeat: \n',mytuple * 5)

print(mytuple[2:4])

for i in mytuple:
    print(i)


print(max(mytuple))








