# Представим Вы создали сайт онлайн курсов по Python.
# Ваша задача спросить у пользователя Python ФУНКЦИЮ и если такая есть исполнить
# и вернуть пользователю результат иначе сказать что в Python такой функции нет!
try:
    a = eval(input('введите фунцию '))

except NameError as e:
    print(e, 'в Python такой функции нет!')