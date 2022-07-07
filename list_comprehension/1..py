er_list = [15, 24, 81, 132, 196, 214]
list = []
new_list = [x for x in range(1,255) if x not in er_list]
print(new_list)