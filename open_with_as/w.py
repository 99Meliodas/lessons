with open('w.txt', 'w') as file:
    file.write('123')
with open('w.txt', 'r') as file:
    if 'w' in file.read():
        print('Да, в тексте есть w')
    else:
        print('Нет, в тексте нет w')

