#!/bin/python3

l=[1,2,3,4]
list2=[56,78,"FreeBSD"]

while True:
	print("Select: \n 1. To insert value in the list.\n 2.To insert value in specific index\n 3. Delete element from the list.\4. Exit")
	choice1=int(input("Enter your choice :"))
	if choice1==1 :
		ele1=input("Enter element to be append: ")
		l.append(ele1)
		print(l)

	if choice1==2 :
		ele2=input("Enter element to be append : ")
		pos2=int(input("Enter position : "))
		l.insert(pos2,ele2)
		print(l)
	if choice1==3 :
		ele3=input("Enter element to be remove : ")
		l.remove(ele3)
	if choice1==4:
		print(l)
		print("Exiting from Application")
		break
	else:
		print("Invalid choice")
		
		print(l)
		print("Second list: ",list2)
		print("List Applend:")
		print(l.append(list2))
		print("List Extend: ")
		print(l.extend(list2))
		continue
list3=[]
num=int(input("How many number\'s square you want?"))
for i in range(num):
	element1=int(input("Enter value:"))
	list3.append(element1)

list3 = list(map(int, list3))
print(list3)
val=[x**2 for x in list3]
print(val)



