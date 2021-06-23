import hashlib
sql='app_id=app_1614147430&app_secret=cfdc41489f9ae8bad6e5d81eb437a05be952ebd7&nonce=60329869&product=352741&source=vm_hr&timestamp=1614411864713&vmhr_order_id=637500374647448602'
signature = hashlib.md5(sql.encode()).hexdigest().upper()
print(signature)