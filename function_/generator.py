import random
list_1 = '145790'
number = ['0', '4', '4', '4']
def gen_numbers():
    for i in range(6):
        number.append(random.choice(list_1))
    print(''.join(number))

gen_numbers()
