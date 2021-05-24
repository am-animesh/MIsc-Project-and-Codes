# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:10:45 2021

@author: animesh
"""

def a_arrange(a,b):
    n = 0
    if len(a)<=len(b):
        for i in range(0,len(a)):
            a1 = ord(a[i])-96
            a2 = ord(b[i])-96
            if a1!=a2:
                if a1<a2:
                    n = 0
                    break
                elif a1>a2:
                    n = 1
                    break 
    else:
        for i in range(0,len(b)):
            a1 = ord(a[i])-96
            a2 = ord(b[i])-96
            if a1!=a2:
                if a1<a2:
                    n = 0
                    break
                elif a1>a2:
                    n = 1
                    break 
    return n 

def n_arrange(a,b):
    if a<=b:
        n1 = 0
    elif a>b:
        n1 = 1
    return n1

#f = open('alpha_arrange.txt', 'r')
f = open('try.txt', 'r')
f1 = f.read()
f2 = f1.split()
f3 = []
f4 = []
f5 = []
f6 = []

for i in range (len(f2)):
    if (i%2) == 0:
        f3.append(f2[i])
        f5.append(f2[i])
    elif (i%2) != 0:
        f4.append(f2[i])
        f6.append(int(f2[i]))      
#__Alpha arrange__
for j in range (len(f3)-1):
    min_index = j
    for i in range(j+1, len(f3)):
            n = a_arrange(f3[min_index],f3[i])
            if n == 1:
                f3[min_index], f3[i] = f3[i], f3[min_index]
                f4[min_index], f4[i] = f4[i], f4[min_index]
                
#__Number arrange__
for i in range(len(f6)-1):
    min_index1 = i
    for j in range(i+1,len(f6)):
        n1 = n_arrange(f6[min_index1],f6[j])
        if n1 == 1:
            f5[min_index1], f5[j] = f5[j], f5[min_index1]
            f6[min_index1], f6[j] = f6[j], f6[min_index1]
        
        
print('Alphabetical sorting:\n')                
for i in range(len(f3)):
    print(f3[i],' ',f4[i])
print('\n')    
print('Numeric sorting:\n')
for j in range(len(f5)):
    print(f6[j],' ',f5[j])
            
#print(f3)
#print(f4)
            
    

    
    
    
