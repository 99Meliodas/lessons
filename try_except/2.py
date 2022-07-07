#Code #1:

at = 10
inh = 15
wo = 20
try:
    for e in range(-at, at):
        print(wo / e)
    if at > 5:
        print("at > 5")
except Exception as a:
    print('Erroe=e', a)