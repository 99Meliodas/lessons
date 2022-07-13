# Создайте функцию которая принмает тип данных dictionary,
# но возвращает два Tuple в одном из них все ключи, в другом только значения.
def type_(a = {}):
    a = list(dict.keys(a)), list(dict.values(a))
    print(a)
type_({1: 'nurtai', 2: 'handsome', 3: 'nice', 4: 'good'})
