# Создайте функцию которая принимает слово и создаёт файл с таким именем в той же директории,
# где был запущен Ваш .py файл.
def name_file(str):
    with open(str, 'w') as file:
        file.write('')

name_file('kroko')
