# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 20:25:56 2020

@author: animesh
"""
#Input vcf file into the program
f = 'inputVideo/Contacts.vcf'
#f =  'inputVideo/c1.txt'

file = open(f,"r") 
fout = open('inputVideo/c1.csv','w+')

intro = 'BEGIN:VCARD\n'
outro = 'END:VCARD\n'

#Defining custom class to input the data
#All the variables of class are defined as strings
class vcards:
    name =  ''
    fn = '' 
    tel1 = ''
    tel2 = ''
    tel3 = ''
    email = ''

vcard=[]
l1 = ''
l2 = ''

k1 = 'N'
k2 = 'FN'
k3 = 'TEL;HOME'
k4 = 'TEL;WORK'
k5 = 'TEL;CELL'  
k6 = 'EMAIL'

j = 0
#Inputting header row into csv file
fout.write('Name,FN,Tel1,Tel2,Tel3,Email')

#Creating instance of class
vcard = vcards()

#Outer while loop is used for traversing vcf file one vcard at a time
while True:
    #print('we are here')
    l1 = file.readline()
    #splitting vcf file into keyword and value using colon as delimiter
    b = l1.split(':')
    #print(l1)
    if not l1:
        break
    #Checking for beginning of vcard
    if l1==intro: 
        l2 = file.readline()
        #print('we are here l2')
        #print(l2)
        #Inner while is used to traverse the current vcard and assign data to class by processing keywords
        while l2 != outro:
            a = []
            a = l2.split(':')
            print(a)
            #We use an if else statement to check the line of vcf file to process keyword and assign
            #value to each element of class
            if a[0]==k1:
                vcard.name = a[1][-1]
                #print(vcard.name)
            elif a[0]==k2:
                vcard.fn = a[1][:-1]
                #print('done',a[1],vcard.fn)               
            elif a[0]==k3:
                vcard.tel1 = a[1][:-1]         
            elif a[0]==k4:
                vcard.tel2 = a[1][:-1]  
            elif a[0]==k5:
                vcard.tel3 = a[1][:-1]
            elif a[0]==k6:
                vcard.email = a[1][:-1]  
            l2 = file.readline()
    #print(vcard.fn)
    #We take all assigned values and we concatenate into a single string and write it into the file
    # Each vcard from vcf file will be created as a single line in csv file
    wline = vcard.name + ','+vcard.fn+',' + vcard.tel1 + ',' + vcard.tel2 + ',' + vcard.tel3 + ','+ vcard.email
    fout.write(wline)

fout.close()
    
       
       
    