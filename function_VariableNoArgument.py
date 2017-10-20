#!/bin/python3
tup=[];
def varLengthArgs(*vargs):
	print("At function-->You entered :")
	val=tuple(vargs)
	print(val)
	return True
print("Outside function-->")
for i in range(5):
	num=int(input("Enter Integer Number: "))
	tup.append(num)

varLengthArgs(tup)
