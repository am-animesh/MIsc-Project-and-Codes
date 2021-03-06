# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 23:23:41 2021

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

#Function to find the parpendicular distance of given point from line
#(x1,y1) and (x2,y2) are the 2 popints on the line and (x0,y0) is the given point
def line_dist(x1,y1,x2,y2,x0,y0):
    numerator = ((x2-x1)*(y2-y0)) - ((x1-x0)*(y2-y1))
    denominator = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    d = numerator/denominator
    return d

#Function for finding distance of circle from point
#r is radius of circle, (x1,y1) is the center of the circle
#(x,y) is the given point
def circle_dist(r,x1,y1,x0,y0):
    d = np.sqrt((x0-x1)**2 + (y0-y1)**2)#Distance between point and center of circle
    ad = d-r
    return ad

#This for loop will traverse the list lines and find the parpendicular distance of each 
#line from the point
for i in range(0,l1):
    x1 = objects.lines[i][0]
    y1 = objects.lines[i][1]
    x2 = objects.lines[i][2]
    y2 = objects.lines[i][3]
    x0 = objects.pts[0]
    y0 = objects.pts[1]
    d1 = line_dist(x1,y1,x2,y2,x0,y0)
    distance1.append(d1)

#This loop traverses the list of circles and finds the distance of each circle from the point    
for i in range(0,l2):
    r = objects.circles[i][0]
    x1 = objects.circles[i][1]
    y1 = objects.circles[i][2]
    x0 = objects.pts[0]
    y0 = objects.pts[1]
    d2 = circle_dist(r,x1,y1,x0,y0)
    distance2.append(d2)

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