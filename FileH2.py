#!/bin/python3

import os
conf=[]
demon=[]
for f in os.listdir('/etc'):
	if f.endswith('.d'):
		demon.append(f)
	if f.endswith('.conf'):
		conf.append(f)
print(conf)
print(demon)
