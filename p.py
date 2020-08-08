# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:51:28 2020

@author: ASUS
"""
v=()
b={1:'10',2:'20',3:'30'}
import matplotlib.pyplot as p
v=b.values()
x=[]
y=[]
print(v)
for i in list(set(v)):
    x.append(i)
    y.append(v.count(i))
    print(i.v.count(i))
p.plot(x,y)
p.show()