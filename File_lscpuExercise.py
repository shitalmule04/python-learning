#!/bin/python3

#write code which will open the file in read only mode and then read the file line by line and find out the
#number of CPU(s).
#

import os
import sys

def command_run(path):
        args=sys.argv[1:]
        if args[0]=='-lscpu':
                contents=None
                with open(path,'r') as f:
               	        contents=f.read()
                        print(contents)
                f.close()
                return True
        else:
                print("Please pass argument \'lscpu\'")
                sys.exit(-1)
                return False
        sys.exit(0)

path="/proc/cpuinfo"
val=command_run(path)
print("Execution Status",val)
