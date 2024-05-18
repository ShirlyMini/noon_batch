import random
import string

# print(string.ascii_letters)#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)#0123456789
# print(random.choice(string.ascii_letters))
# print(random.choice(string.digits))
# <leng of 8 string>@gamil.com
email = []
for i in range(8):
    email.append(random.choice(string.ascii_letters+string.digits))
print("".join(email))

