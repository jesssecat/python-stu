import hashlib
hash = hashlib.md5()
#hash.update(bytes('admin',encoding='utf-8'))
hash.update(bytes('admin',encoding='utf-8'))
print(hash.hexdigest())
