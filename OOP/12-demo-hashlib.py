import hashlib
md5 = hashlib.md5()
md5.update(b'jesse')
print(md5.hexdigest())
