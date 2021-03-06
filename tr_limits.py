# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:20:35 2021

@author: animesh
"""
'''We use the principle of areas to find whether given point is inside or outside triangle.
   We form three small triagles using the point and one side of the given triangle.
   If point is inside, sum of areas of the small triangles = area of big triangle
   If point is outside, sum of areas of the small triangles > area of big triangle'''

import numpy as np
#Given point
pt = [0,4.0001]
#Given triangle
trl = [[0,0] , [0,4] , [4,0]]

#Definig a function to find area of a triangle using Heron's Formula
def area(a, b, c):
    #Finding length of each side using distance formula
    side1 = np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)  #AB
    side2 = np.sqrt((b[0]-c[0])**2 + (b[1]-c[1])**2)  #BC
    side3 = np.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2)  #AC
    s = (side1 + side2 + side3)/2   #Semi perimeter
    ar = np.sqrt(abs(s*(s-side1)*(s-side2)*(s-side3)))   #Heron's formula
    return ar

a = area(trl[0] , trl[1] , trl[2])   #Area of given triangle
#Areas of the three smaller triangles formed
a1 = area(pt , trl[0] , trl[1])
a2 = area(pt , trl[1] , trl[2])
a3 = area(pt , trl[2] , trl[0])

a4 = a1+a2+a3

#Because of errors appearing due to precision of calculation, we may obtain false outputs,
#especially for the inside trangle case, as it is a equality condition of 2 floating point numbers.
#Due to this we have to define a permissable error and 
#compare our obtained error to that. This gives us accurate output with a arbitrarily small fuzzy boundary.
delta = 1e-10*a   # define small error margin relative to coordinate

if a4 > a + delta :
    print('Given point is outside triangle')
else:
    print('Given point is inside triangle')