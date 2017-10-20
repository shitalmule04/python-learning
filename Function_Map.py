#!/bin/python3

# using map(aFunction, aSequence)

items=[]
def sqr(x): 
	return x ** 2

cnt=int(input("How many numbers?"))

for i in range(cnt):
	num=float(input("Enter Any Number :"))
	items.append(num)
print(items)	
print(list(map(sqr, items)))
