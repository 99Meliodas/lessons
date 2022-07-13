# Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.
def connect_dicts(a = {}, b = {}):
    a.update(b)
    print(a)

connect_dicts({1: 'nurtai', 2: 'handsome'}, {3: 'nice', 4: 'good'})
