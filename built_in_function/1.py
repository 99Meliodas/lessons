# Представьте Вы хотите взять какой-то набор данных и переконвертировать его в SET для удаления
# дубликатов, возьмите values и проверьте каждый ли элемент доступен для конвертации. Создайте список.
# Проитерируйте values. Если объект в списке можно переконвертировать добавьте True в новый список
# иначе добавьте False.
# После, с помощью функции all() скажите можно ли конвертировать values в SET?
new_list = []
def convert(*values):
    for i in values:
        if type(i) == int or type(i) == float or type(i) == str or type(i) == set or type(i) == dict:
            new_list.append(True)
        else:
            new_list.append(False)
    if all(values) == True:
        print('можно')
    print(new_list)
convert("TURUSBEKOVA 109/1", 10, 1005, ["TABLES", "CHAIRS"], 23.00)

