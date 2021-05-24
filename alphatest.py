# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:54:27 2021

@author: anime
"""

s1 = 'qanu'
s2 = 'pintu'
no = [11, 3, 2, 56, 7, 100, 0]
#if len(s1)<len(s2):
#    for i in range(0,len(s1)):
#            n1 = ord(s1[i])-96
#            n2 = ord(s2[i])-96
#            if n1!=n2:
#                if n1<n2:
#                    print(s1, ' ', s2)
#                    break
#                elif n1>n2:
#                    print(s2, ' ', s1)
#                    break

'''def arrange(a,b):
    if len(a)<=len(b):
        for i in range(0,len(a)):
                a1 = ord(a[i])-96
                a2 = ord(b[i])-96
                if a1!=a2:
                    if a1<a2:
                        n1 = a
                        n2 = b
                        break
                    elif a1>a2:
                        n1 = b
                        n2 = a
                        break 
    else:
                for i in range(0,len(b)):
                    a1 = ord(a[i])-96
                    a2 = ord(b[i])-96
                    if a1!=a2:
                        if a1<a2:
                            n1 = a
                            n2 = b
                            break
                        elif a1>a2:
                            n1 = b
                            n2 = a
                            break 

    return n1,n2'''
    
def narrange(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i+1,len(n)):
            if n[min_index]>n[j]:
                n[j],n[min_index] = n[min_index],n[j]

narrange(no)
print(no)
#a = []
#a.append(arrange(s1,s2))
#a1,a2 = arrange(s1, s2)
        