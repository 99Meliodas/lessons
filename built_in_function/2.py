# Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел.
set_1 = []
def minimum():
    for i in range(5):
        a = int(input('введите число '))
        set_1.append(a)
    print(min(set_1))


minimum()