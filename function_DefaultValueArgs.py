#!/bin/python3

def f(a, data=None):
	if data is None:
		data = []
		data.append(a)
		print(data)
	return data
num=input("Enter Data:")
f(num)

