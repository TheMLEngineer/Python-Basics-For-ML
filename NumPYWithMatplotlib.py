# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 17:56:35 2018

@author: KarthikM
"""

import matplotlib.pyplot as plt
import numpy as np

m=3
c=4
x=np.linspace(1,20)

y = m*x +c

plt.title('Visualisation Example')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x,y)
plt.show()




plt.title('Visualisation Example')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x,y,'--')
plt.show()


plt.title('Visualisation Example')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x,y,'.-')
plt.show()



plt.title('Visualisation Example')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x,y,'.')
plt.show()

opt = ['--','.','-','.-','|','p','D','1','2','s']
color1 = ['r','g','y','b','r','g','y','b','r','g','y']

for i in range(len(opt)):
    m=3
    c=4
    x=np.linspace(1,20)
    y = m*x +c
    plt.title('Visualisation Example')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.plot(x,y,opt[i],color=color1[i])
    plt.show()


x = [10,12,14]
y = [6,12,15]

x1 = [11,13,15]
y1 = [8,9,19]


plt.bar(x,y,align='center')
plt.bar(x1,y1,align='center')

plt.title('Bar chart')
plt.xlabel('X axis')
plt.label('Y axis')
plt.show()















































