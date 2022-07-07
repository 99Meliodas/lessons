dict = {}
ll = []
pl = []
a = 1
while a <= 6:
    login = input()
    ll.append(login)
    password = input()
    pl.append(password)
    a += 1
dict = {i:k for i in ll for k in pl}

print(dict)