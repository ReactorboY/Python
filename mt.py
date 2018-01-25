# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:41:41 2018

@author: sharda
"""

a = [[5,1], [2,1]]
b = []
c = [[0,0], [0,0]]
count = 0

for i in range(0,len(a)) :
    b=b+a[i]
print (b)

for i in range(0, len(b)-1):
    for j in range(0, len(b) - 1):
        if (b[j] < b[j+1]):
            temp = b[j]
            b[j] = b[j+1]
            b[j+1] = temp

print(b)
#print (b)
# print [5,1,2,1]    
