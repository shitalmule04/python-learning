#!/bin/python3
global total
total=1234;
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print("Outside the function global total : ", total)
