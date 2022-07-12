def fibonachi(x):
    a, b = 1, 1
    for i in range(x):
        yield a
        a, b = b, a + b
list_fibonachi = list(fibonachi(10))
print(list_fibonachi)

