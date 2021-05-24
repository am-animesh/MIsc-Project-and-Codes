# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:50:55 2021

@author: animesh
"""
'''We have to check if given number is prime or not. Initially we check if given number(n) is divisible by 
   any of the single digit prime numbers. If not, we enter the larger search region. We have to search 
   only between 11 and sqrt(n). For every single digit prime number that is not a factor of n, we do not 
   have to check if its multiples are factors of n. Like this we reduce the number of calculations required
   to get the output. 
   One more addition we can make (not implemented here) is that when we find that a given element inside the search region is not
   a factor of n, we can append it into the array of single-digit primes so that its multiples are also eliminated from the search 
   region. But this increases the memory required by the program. '''   

n = 5915587277  #Number to be checked
flag = 0  #This will be used to count the number of factors of n

# pcheck is an array that contains all the prime numbers between 0 and 9. 
# If n is divisible by any of them its not prime
# If its not divisible by any of them, we can skip the multiples of all these 
# numbers while traversing the search region.
pcheck = [2,3,5,7]  

# For loop to check if n divisible by any element in pcheck 
for i in pcheck:
    if n%i == 0:
        flag += 1
        break

# If its not divisible flag will be zero and number may be prime. So we continue search
if flag == 0:
    #For loop traverses search region
    for j in range(11, round(n**0.5)+1, 2):
        flag1 = 0
        # For loop checks if reference number is multiple of any element of pcheck
        for k in pcheck:
            if j%k == 0:
                #If it is a multiple, flag1 becomes 1
                flag1 = 1
        #Checks for value of flag1
        #If flag1 != 1, it checks if reference number is factor of n
        if flag1 == 0:
            if n%j == 0:
                flag += 1
                break

#If flag is greater than zero n is not prime
if flag > 0: 
    print('Given number is not prime')
else:
    print('Given number is prime')