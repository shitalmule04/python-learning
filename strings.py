#!/bin/python3

str1=input("Enter any setence: ")
print("String Title : "+str1.title())
print("To upper case: "+str1.upper())
print("To lower case: "+str1.lower())
print("To swap cases: "+str1.swapcase())
print("Is Alpha Numeric?  %r " %str1.isalnum())
print("Contains Aplabets only? %r " %str1.isalpha())
print("Whether charecters are digit? %r "%str1.isdigit())
str4=str1
str2=str1.split(" ")
print("Splitted string: ",str2)

str3=input("Enter word to be find: ")
print("Number present at position %d "%(str1.find(str3)))
print("Number of words in given line : %d" %(len(str4.split(" "))))

