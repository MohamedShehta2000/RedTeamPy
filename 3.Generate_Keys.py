#!usr/bin/python3
import rsa 
publickey, privatekey= rsa.newkeys(512)
print(publickey)
print(privatekey)