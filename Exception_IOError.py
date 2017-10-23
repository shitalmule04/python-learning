#!/bin/python3

try:
        f=open('abc.txt')
        s=f.readline()
        i=int(s.strip())
except (IOError, ValueError):
        print("An I/O error or a ValueError occurred....!!")
except:
        print("An unexpected error occurred..!!")
        raise
