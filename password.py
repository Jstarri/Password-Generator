import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

pwd_length = 8
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)