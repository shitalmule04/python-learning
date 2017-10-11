#!/bin/python3

import sys
args=args=sys.argv[1:]
args[0]=int(args[0])
args[1]=int(args[1])

#Arithmetic  Operator
print("%d + %d = %d" %(args[0],args[1],args[0]+args[1]))
print("%d - %d = %.2f" %(args[0],args[1],args[0]-args[1]))
print("%d * %d = %.2f" %(args[0],args[1],args[0]*args[1]))
print("%d / %d = %.2f" %(args[0],args[1],args[0]/args[1]))
print("%d // %d = %d" %(args[0],args[1],args[0]//args[1]))

#Logical Operator
print("%d + %d = %d" %(args[0],args[1],args[0]+args[1]))
