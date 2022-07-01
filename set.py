dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print (dates_of_birth)

a = set()
a = {1,2,3}
b = set()
b = {'1','2'}
c = set()
c = {'jack', 'jim'}
d = set()
d = {'789'}
a.update(b, c, d)
print(a)
print()


farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2.difference(farm_1))


k = set()
k = {'1', 'k', 'f', '134', 'lol'}
k.add('nurtai')
k.pop()
print(k)
'''
l = set()
for i in range(10):
    i = input('->')
    l.add(i)
m = frozenset()
m = l
print (m)
'''

farm_3 = set()
farm_3 = farm_1.intersection(farm_2,)
print(farm_3)
farm_4 = set()
farm_4 = farm_1.difference(farm_2)
print(farm_4)

