import hashlib

hash_md5 = hashlib.md5()
hash_sha1 = hashlib.sha1()
hash_sha224 = hashlib.sha224()
hash_sha256 = hashlib.sha256()
hash_sha384 = hashlib.sha384()
hash_sha512 = hashlib.sha512()

file_location = raw_input("Enter file location: ")
option = raw_input("****option menu****\n1) MD5\n2) SHA1\n3) SHA224\n4) SHA256\n5) SHA384\n6) SHA512\n")

print "\n\n*********************************************"
if option == '1':
	with open(file_location) as file_Object:
		for line in file_Object:
			hash_md5.update(line)
	print "MD5: " + hash_md5.hexdigest() 
elif option == '2':
	with open(file_location) as file_Object:
		for line in file_Object:
			hash_sha1.update(line)
	print "SHA1: " + hash_sha1.hexdigest()
elif option == '3':
	with open(file_location) as file_Object:
		for line in file_Object:
			hash_sha224.update(line)
	print "SHA224: " + hash_sha224.hexdigest()  
elif option == '4':
	with open(file_location) as file_Object:
		for line in file_Object:
			hash_sha.update(line)
	print "SHA256: " + hash_sha256.hexdigest()  
elif option == '5':
	with open(file_location) as file_Object:
		for line in file_Object:
			hash_sha384.update(line)
	print "SHA384: " + hash_sha384.hexdigest() 
elif option == '6':
	with open(file_location) as file_Object:
		for line in file_Object:
			hash_sha512.update(line)
	print "SHA512: " + hash_sha512.hexdigest() 
print "*********************************************\n"



