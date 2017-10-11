#!/bin/python3

import math

#Factorial
num1 = int(input("Enter any number: "))
print("Factorial of  %d is %d" %(num1,math.factorial(num1)))

#Power Functions
num2=int(input("Enter number:"))
print("e**%d is %.2f" %(num2,math.exp(num2)))
print("%d raised to power of %d is %d" %(num1,num2,math.pow(num1,num2)))

#Angular functions

num3=int(input("Enter angle :"))
print("%d degree equal to %.4f radians" %(num3, math.radians(num3)))
print("%d radians equal to %.4f degree" %(num3, math.degrees(num3)))
