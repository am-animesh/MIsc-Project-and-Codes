# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:11:50 2021

@author: animesh
"""
'''For finding the nearest line we find the parpendicular distance of each line from the point.
   We put all the distances into a list.
   For finding the nearest circle, we find the distance of the centre from the point and we 
   subtract the radius of the circle from it. We put all these distances into a seperate list.
   We now find the minimum from each of those lists. We compare the minima and take the 
   smallest one . Based on its index we can tell which is the nearest element.'''
   
import numpy as np

class objects:
    pts = [3,4]
    #Lines defined as [[x1,y1,x2,y2](line1) , [x1,y1,x2,y2](line2) , ...]
    lines = [[5,6,1,2] , [7,10,3,2] , [12,11,4,3]]
    #circles defined as [(r,x,y)(circle1) , (r,x,y)(circle2) , ...]
    circles = [(1,18,0) , (4,12,23) , (6,5,16)]

#Distances of lines from point    
distance1 = []
#Distances of circles from point
distance2 = []
l1 = len(objects.lines)
l2 = len(objects.circles)

for i in range(0,l1):
    #Formula for finding parpendicular distance from line and creating list
    distance1.append((((objects.lines[i][2]-objects.lines[i][0])*(objects.lines[i][1]-objects.pts[1]))
    -((objects.lines[i][0]-objects.pts[0])*(objects.lines[i][3]-objects.lines[i][1])))/np.sqrt
    (abs(((objects.lines[i][2]-objects.lines[i][0])^2)+((objects.lines[i][3]-objects.lines[i][1])^2))))
for i in range(0,l2):
    #Formula for finding distance of center - radius and creating list
    distance2.append(np.sqrt(abs(((objects.circles[i][1]-objects.pts[0])^2)
    -((objects.circles[i][2]-objects.pts[1])^2))-objects.circles[i][0]))

#Finding minimums    
m1 = min(distance1)
ind1 = distance1.index(min(distance1))

m2 = min(distance2)
ind2 = distance2.index(min(distance2))

#Comparing minimums
if m1>m2:
    minele = objects.lines[ind1]
else:
    minele = objects.circles[ind2]
    
#Final output    
print(minele)