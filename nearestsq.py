# -*- coding: utf-8 -*-

'''We use the concept of narrowing down the region for searching using 
   the number of digits that the input number has. Using those as the limits we 
   we apply the Newton-Raphson method to converge at the required point. '''
n = 132
l = len(str(n))
#The following if-else structure is for finding the limits of the search region 
# Lower limit will be the largest l-1 digit square number and upper limit will be
# smallest l+1 digit square number.
if l%2 ==0:
    l_lim = 3*(10**((l/2)-1))
    u_lim = 10**(l-1)
else:
    l_lim = 10**(l-2)
    u_lim = 3.5*10**(l-2)
    
x1 = l_lim
y1 = l_lim**2
x2 = u_lim
y2 = u_lim**2
output = 0

while output==0:
    #Finding the slope of the the line formed by taking the two limits as 2 points on the line
    m = (y2-y1)/(x2-x1)
    #Applying Newton-Raphson formula
    x0 = (((m*x2)+n-y2)/m)
    #Delta is used for checking if the seed data is on the left or right of required data
    delta = (x0**2)-n
    #If-else structure used for changing the limits based on where required data lies in comparison
    # to seed data
    if delta>0 and delta<1 or delta>-1 and delta<0:
        output = round(x0)
        break
    elif delta>1:
        x2 = x0
        y2 = x2**2
    elif delta<-1:
        x1 = x0
        y1 = x1**2

#Required output        
print(output)   