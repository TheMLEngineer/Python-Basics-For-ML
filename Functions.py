# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 02:22:09 2019

@author: kmuthu2
"""

def split_fn(any_list):
    str_items = []
    num_items = []

    for i in any_list:
        if isinstance(i,float) or isinstance(i,int):
            num_items.append(i)
        elif isinstance(i,str):
            str_items.append(i)
        else:
            pass
    return num_items,str_items
    print(num_items)
    print(str_items)


#Using fn
items = [1,234,456.34,'hi','hello','123',1234]
print(split_fn(items))