# -*- coding: utf-8 -*-
"""
CATT_Formatter.py
Copyright 2017, Peter Dodds

This software is provided as tool to more easily format SU2CATT output when 
material assignment is not done within the model

THIS SOFTWARE IS PROVIDED "AS IS" AND WITHOUT ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
"""

import os
#import fileinput

SU2CATTString = "no_name" #default material name from SU2CATT

folder = os.getcwd()

for filename in os.listdir(folder): #for every file in the directory
    if filename.endswith('.geo'): #if the file has a .geo extension
       newname = filename.replace('.geo', '.txt') 
       output = os.rename(filename, newname) 
       
       with open(newname,'r') as file: 
           filedata = file.read()
           #if the file has the SU2CATTString in it, replace that with the filename less the extension (4 characters)
           filedata = filedata.replace(SU2CATTString,newname[:-4]) 
       with open(newname,'w') as file: #write the file and close it
           file.write(filedata)
           file.close()
          
        
for filename in os.listdir(folder): #for every file in the directory
    if filename.endswith('.txt'): 
       newname = filename.replace('.txt', '.geo') 
       output = os.rename(filename, newname) #rewrite the file in the folder

print('File clean-up complete.')
