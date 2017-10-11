#!/bin/python
reversedNum=0
num=int(input("Enter integer number:"))
num2=num
while num!=0 :
	remainder=num%10
	reversedNum=reversedNum*10+remainder
	num//=10
print(" Reverse of %d is %d" %(num2,reversedNum))
