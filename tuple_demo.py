#!/bin/python3

data=("Red Hat Academy", "ritinlug", "RIT")
a1,a2,a3=data
msg = "{0} and {1} introduced at {2}".format(a1,a2,a3)
print(msg)
print("Inserting Values in tuple")
val=(input("Enter value: "))

#Convert tuple into tuple
l = list(data)
l.append(val)

#Add conerted list into tuples
data=tuple(l)
print("After inserting value tuple is",data)

