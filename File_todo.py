#!/bin/python3
import sys
import os

args=sys.argv[1:]
if args[0]=='-a':
	data=input("Enter data to be write :")
	with open('todo.text','w') as f:
		f.write("\n"+data+" ".join(args[1:]))
if args[0]=='-v':
	contents=None
	with open('todo.text','r') as f:
		contents=f.read()
	print(contents)

if args[0]=='-d':
        data2=input("Enter data to be delete: ")
