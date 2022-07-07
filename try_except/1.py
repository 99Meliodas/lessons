a = [1,2,3,4,5]
try:
    a = 'name' * 42
    print(a[6])
    print(kok)
except(TypeError, IndexError, NameError) as e:
    print(TypeError, IndexError, NameError)
