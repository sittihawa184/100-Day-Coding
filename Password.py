import random
passlen = int(input("enter the length of password : "))
s="hawa"
p = " ".join(random.sample(s,passlen ))
print(p)
