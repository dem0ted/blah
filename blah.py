import sys
import hashlib
f= open(str(sys.argv[2]))
with open(str(sys.argv[2])) as file:
	blah = f.read()
	md5result = hashlib.md5(blah.encode())
	sha1result = hashlib.sha1(blah.encode())
	sha256result = hashlib.sha256(blah.encode())
	print("MD5 is: ",md5result.hexdigest())
	print("SHA1 is: ",sha1result.hexdigest())
	print("SHA256 is: ",sha256result.hexdigest())