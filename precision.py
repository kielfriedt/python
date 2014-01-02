#Addition of two numbers with high precision: input is a string in the format of "A+B" where A and B are float numbers with high precision (e.g., 1.234567890123456789012345678901234567890...). Output is a string that represents the result.

from mpmath import *

mp.dps = 50 # setting decimal places for highest percision 
input = raw_input("enter as A+B")
values = input.split('+') #split string by + allowing the two strings to be coverted
print str(mpf(value[0])+mpf(value[1]))#prints value of A+B in full precision as string

# sites
# code.google.com/p/mpmath
# stackoverflow.com