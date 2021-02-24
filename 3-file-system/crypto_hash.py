##################################################
# hashlib
##################################################

# hashlib works with multiple crypto hashing algorithms

# md5
# To calculate the MD5 hash, or digest, for a block of data (here a unicode string converted to a byte string), first create the hash object, then add the data and call digest() or hexdigest().

import hashlib

form hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())

# sha
h = hashlib.sha1()
h.update(lorem.encode('utf-8'))
print(h.hexdigest())

# binary digests
import base64
import hmac
import hashlib

hash = hmac.new(
    b'secret-key',
    body,
    hashlib.sha1,
)

digest = hash.digest()
print(base64.encodebytes(digest))

# Simulate a readable socket or pipe
