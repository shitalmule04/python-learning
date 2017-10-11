#!/bin/python3

def bubbleSort(list1,count1) :
	for i in range(0,count1-1):
		for j in range(0,count-1-i):
			if list1[j]>list1[j+1]:
				list1[j],list1[j+1]=list1[j+1],list1[j]
	return(list1)
l=[]
count=int(input("How many Numbers?"))
for i in range(count):
	val=int(input("Enter Number: "))
	l.append(val)
print("list is",l)
print("After Bubble Sort:") 
print(bubbleSort(l,count))
