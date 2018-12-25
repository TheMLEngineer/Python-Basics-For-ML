# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 16:40:57 2018

@author: KarthikM
"""

import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
type(a)
a1 = np.arange(15).reshape(5,3)
a.shape
a.reshape(15,1)
a.transpose()
a3 = a.dot(a1)

a4 = np.sin(a3)
a5 = np.cos(a3)


#sin2 + cos2 =1

a6 = a4**2 + a5**2 

np1 = np.zeros((10,5),dtype = int)
np2 = np.ones(10,dtype = int)
