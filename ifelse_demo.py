#!/bin/python3

''' WAP that should take one command line argument, if argument is Linux it should show Red Hat, if Fedora then output as Linux, if no argument then it should show message type Linux | Fedora as input '''

import sys

args=sys.argv[1:]

if args[0]=='Linux' :
	pass
	print("Red Hat")
elif args[0]=='Fedora':
	pass
	print("Linux")
else:
	print("Please type Linux | Fedora")
