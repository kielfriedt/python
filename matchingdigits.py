#Given a number, find the next higher number which has the exact same set of digits as the original number. For example: given 38276 return 38627.

int_value = raw_input("please enter value ")
final_value = int(int_value) # copy inital value to increment later
int_list = map(int, str(int_value)) #seperate value into digits ex: 123 to [1,2,3]
int_list.sort() # sort list to compare them
final_list = [] #copy list for comparison
# use collections to compare two lists and see if they match also if the length of the two lists differ break because the value checking value is now greater in digits
while int_list != final_list:
    final_value += 1
    final_list = map(int, str(final_value))#after increment of value split it into list to make list compare easier.
    final_list.sort()
    if final_list.length != int_list.length:
        break;

if final_list.length != int_list.length: #If while breaks because of more digits
    print "No values were found in the available digits."
else: # otherwise the result will be the matching values ex: 123 and 132
    print final_value


# sites used
# wiki.python.org
# stackoverflow.com