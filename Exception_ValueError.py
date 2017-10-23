#!/bin/python3

while True:
        try:
                n=input("Enter any integer number: ")
                n = int(n)
                break
        except ValueError:
                print("No valid integer! Please try again ...")
print("Entered Value: %d" %n)
