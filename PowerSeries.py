#!/bin/python3

#To take input from user
x=float(input("Enter the value of x: "))

n=term=num=1
sum=1
while n<=100:
	
	''' term-->present term,multiplying the previous term by x/n, It will decrease as occurance of loop increase'''
	term *=x/n

	#sum-->sum of terms 
	sum+=term
	
	#number of terms
	n+=1

	if term < 0.001:
		'''when term become equal to zero then while loop will be break, It is also called accuracy''' 
print("No of terms= %d and Sum=%f" %(n,sum))
