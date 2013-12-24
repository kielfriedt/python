#!/usr/bin/python
import sys
import socket
import string
import random
from random import randint

#creates random stings of custom length or default 10 
def letter_generator(size=10, chars = string.ascii_letters + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

value_ToIncreaseBy = 0
random_Characters_list = []

#Menu
IP_Address = raw_input("Enter FTP target IP address: ")
options = raw_input("\r*****options menu*****\n1)Display fuzz output\n2)Silent mode\n")

#check to see if IP address is valid
try:
    socket.inet_aton(IP_Address)
    # legal
except socket.error:
	# Not legal
	print "Error: Invalid IP address\n"
	sys.exit()

#seed counter value
counter = randint(2,5)

#creating random increase value
for y in xrange(1,3):
	value_ToIncreaseBy = value_ToIncreaseBy + randint(1,10) 
value_ToIncreaseBy = value_ToIncreaseBy/3


#Creates random fuzz string
while len(random_Characters_list) <= 28:
	#creating random fuzzing text
	random_Characters_list.append(letter_generator(counter*counter))
	#increasing counter towards
	counter=counter+value_ToIncreaseBy

#list of FTP commands
commands = ["MKD", "RMD", "STOR"]

#Creating socket connecting and logs in to ftp server
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect =s.connect((IP_Address,21))
s.recv(1024)
s.send('USER msfadmin\r\n')
s.recv(1024)
s.send('PASS msfadmin\r\n')
s.recv(1024)

# Fuzzing begins here
for command in commands:
	for string in random_Characters_list:
		print "Sending the " + command + " command with " + str(len(string)) + " bytes."
		s.send(command + ' ' + string + '\r\n')
		if options == '1':
		  print "Fuzz string: " + string + "\n"
		s.recv(1024)
s.send('QUIT ftp \r\n')
s.close() #closes socket


