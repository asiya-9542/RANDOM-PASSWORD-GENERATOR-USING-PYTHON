import random
import string

pass_len = 6
charvalues =(string.ascii_letters+string.digits+string.punctuation)

#list comprehension [function for i in range(n)]
password = "".join([random.choice(charvalues) for i in range(pass_len)])
print(password)

