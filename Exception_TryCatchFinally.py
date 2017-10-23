#!/bin/python3

try:
        num=input("Enter number: ")
        num=float(num)
        result=num/0
except ValueError:
        print("You should have given either an int or a float")
except ZeroDivisionError:
        print("Result is Infinity")
finally:
        print("At finally block. There may or may not have been an exception.")
