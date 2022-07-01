languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	if i == 'php':
		print('нашел')
		break    

a = 7
for i in range(5):
	a *= a
print(a)

a = 0
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	print(a,i)
	a += 1

i = 1
for i in range(10):
	i += 1
	print(i)
for i in range(9, 1, -1):
	print(i) 	


names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(len(names)):
	if i % 2 == 0:
		print(names[i])
print()

names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(1, 12, 2):
	print(names[i])
print()


a =int(input())
if 99<a<999:
	print('трехзначное')
elif a > 0 and a % 2==0:
	print('положительное и четное')
elif a % 31 == 0:
	print('без остатка')
elif a>100 and a%17==0 or a>150 and a==13**2:
	print(a)

b = []
print('##########')
for i in range(-100, 100):
	if i % 13 == 0 :
		if i % 2 == 0: 
			i**2
			print(i)
			b.append(i)
print('##########')
a = []
for i in range(-100,100,7):
	if i % 2 != 0:
		print(i)		
		a.append(i)
print(len(a))
print(len(b))

