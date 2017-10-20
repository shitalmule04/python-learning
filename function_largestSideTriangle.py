#!/usr/bin/env python3
import math
def longest_side(a, b):
	"""Function to find the length of the longest side of a right triangle.
	:arg a: Side a of the triangle
	:arg b: Side b of the triangle
	:return: Length of the longest side c as float
	"""
	return math.sqrt(a*a + b*b)

if __name__ == '__main__':
	side1=float(input("Enter side A : "))
	side2=float(input("Enter side B: "))
	print("Side C: %f "%longest_side(side1,side2))
