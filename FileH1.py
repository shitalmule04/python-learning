#!/bin/python3
def write_file(text):
	with open('sample.txt','w') as f:
		f.write(text)
def read_file():
	contents=None
	with open('sample.txt','r') as f:
		contents=f.read()
	return contents

text1="""Shital M. Mule,\nAddress:Chandrapur,Maharashtra\nMob. No:9623711872"""

write_file(text1)
print(read_file())
