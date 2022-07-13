# Написать Функцию которая принимает предложение как аргумент,
# считает количество букв и возвращает сколько символов он ввёл.
# НЕ ИСПОЛЬЗОВАТЬ функцию len()

def length(str_len):
    symbols = 0
    for i in str_len:
        symbols += 1
    print(symbols)
    letters = 0
    for i in str_len.replace(' ', ''):
        letters += 1
    print(letters)
length('hello my dear friend')

