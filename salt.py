import hashlib
import sys

salt = raw_input("Enter Salt value: ")
password = raw_input("Enter password: ")
option = raw_input("****hash type****\n1) MD5\n2) SHA1\n3) SHA224\n4) SHA256\n5) SHA384\n6) SHA512\n")

if option == '1':
	hash = hashlib.md5()
	hash.update(password)
elif option == '2':
	hash = hashlib.sha1()
	hash.update(password)
elif option == '3':
	hash = hashlib.sha224()
	hash.update(password)
elif option == '4':
	hash = hashlib.sha256()
	hash.update(password)
elif option == '5':
	hash = hashlib.sha384()
	hash.update(password)
elif option == '6':
	hash = hashlib.sha512()
	hash.update(password)
else:
	sys.exit()
original_Hash = hash.hexdigest()
hash.update(hash.hexdigest() + salt)
salted_Hash = hash.hexdigest()

print "********************************"
print "Original hash value: " + original_Hash
print "Salted hash: " + salted_Hash
print "********************************\n"