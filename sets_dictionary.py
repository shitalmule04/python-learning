#!/bin/python3

s1=input("Enter elements of first set(space not allowed):")
s2=input("Enter elements of second set(space not allowed):")

set1=set(s1)
set2=set(s2)

print("Entered sets are:\n ",set1)
print("\n",set2)

print("*" * 60)
print("set1 - set2==>", set1-set2)
print("set1 | set2==>",set1|set2)
print(" set1 & set2==> ",set1 & set2)
print("set1 ^ set2 ==> ",set1^set2)
print("*" * 60)

dict1={"Fruit":"Apple", "Flower":"Jasmine","Yellow Dog":"Linux","OS":"RHEL"}
for a,b in dict1.items():
	print("%s-->%s" %(a,b))

print("**Search for data***")
val2=input("Enter value to be searched: ")
if val2 in dict1:
	print("True, Entered value in dictionary..")
else:
	print("False, Entered value no in dictionary, try again..")
