list_1 = ['name', 'age', '1', '19']
def list_cut():
    a = int(len(list_1) / 2)
    list_2 = list_1[:a]
    list_2.reverse()
    list_3 = list_1[a:]
    list_3.reverse()
    print(list_2 + list_3)

list_cut()