#1
text = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
print(text.count(' '))

#2
text = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'"
a = text.split(' ')
print(a)
print(a[0].isalpha())
print(a[1].isalpha())
print(a[2].isalpha())
print(a[3].isalpha())
print(a[4].isalpha())
print(a[5].isalpha())
print(a[6].isalpha())
print(a[7].isalpha())
print(a[8].isalpha())
print(a[9].isalpha())
print(a[10].isalpha())
print(a[11].isalpha())
print(a[12].isalpha())
print(a[13].isalpha())
print(a[14].isalpha())
print(a[15].isalpha())
print(a[16].isalpha())
print(a[17].isalpha())


#3
text = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
print(text.title())


#4
text = 'GitHub'
a = str(input( ))
print(text.split(a))


#5
text = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
print(text.replace('е','3'))

#6
a = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
b =int(len(a) / 2)
c = a[:b]
d = a[b:]
print(c.lower(), d.upper())

#7
a = True
b = str(True)
print(b)
