# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:56:24 2020

@author: animesh
"""

f = 'inputVideo/c1.csv'
file = open(f,"r") 
fout = open('inputVideo/c1.vcf','w+')

vcard1 = []
l1 = ''
#Array of predefined categories of each vcard
k = ['N:','FN:','TEL;HOME:','TEL;WORK:','TEL;CELL:','EMAIL:']
file.readline()
#Each iteration of while will create one vcard
while True:
    vcard2 = []
    l1 = file.readline()
    if not l1:
        break
    #Splitting every line of csv file using comma as delimiter so that we get the distinct value of 
    #each category for the vcard
    vcard1 = l1.split(',')
    size = len(vcard1)
    #Concatenating the keyword and the value to give one field of the vcard
    for i in range(0,size-1):
        vcard2.append(k[i] + vcard1[i]+'\n')
    #Starting a vcard using begin vcard
    fout.write('BEGIN:VCARD\n')
    fout.write('VERSION:2.1\n')
    #For loop will write one vcard at a time into vcf file
    for i in range(0,size-1):
        fout.write(vcard2[i])
    fout.write('END:VCARD\n')
fout.close()