name = input('введите имя файла -> ')
def zapros():
    with open(name, 'w') as file:
        file.write('')

zaprosit = zapros()
print(zaprosit)