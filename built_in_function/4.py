# Вы работаете в Банке и пишите программу которая считает % для кредита.
# Спросите у пользователя сумму займа(не меньше 50 000) и посчитайте сколько нужно будет вернуть
# если % = 3.47, результат округлите до 2 чисел после точки.
# Формула подсчёта переплаты: Сумма * (% / 100)
def zaim():
    summa = int(input('введите сумму займа '))
    if summa >= 50000:
        vozvrat = summa * (3.47/100)
        print(round(vozvrat))

zaim()