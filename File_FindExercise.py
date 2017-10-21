#!/bin/python3

#how many CPU(s) are there in your processor? or what is the model name? Let us write some code
#which can help us to know these things.

import os
import sys

def find_Strings(path):
        word1='CPU(s) '
        word2='Model name '
        line_no=0 
        with open(path,'r') as f:
                for line in f:
                        line_no+=1
                        if line.find(word1):
                              #print("Found in line %d"  %(line_no)) 
                              print(line)
                        if word2 in line:
                              #print("Found in line %d"  %(line_no))
                              print(line) 
        f.close()        
path="/proc/cpuinfo"
print(path)
find_Strings(path)     
