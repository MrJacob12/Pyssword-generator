import random

all_s = "123456789!@#$%^&*()_+=-{}[]:;<>/?~`"
alp = "QWERTYUIOPASDFGHJKLZXCVBNM"
a = alp.lower()
a += alp
a += all_s

length = input("Length: ")
password = ''.join(random.choice(a) for i in range(int(length)))
print(password)