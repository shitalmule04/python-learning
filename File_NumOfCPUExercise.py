#!/bin/python3

#write code which will open the file in read only mode and then read the file line by line and find out the
#number of CPU(s).
#

import os
import sys

def find_NoOfCPU(path):
        word='cpu cores	'
        with open(path,'r') as f:
                for line in f:
                        if word in line: 
                              print(line) 
                f.close()     
path="/proc/cpuinfo"
print(path)
find_NoOfCPU(path)     
