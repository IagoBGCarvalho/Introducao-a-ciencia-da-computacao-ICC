def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

x = int(input())
y = int(input())

result = compare(x, y)

if result == 1:
    print("x e maior que y")
elif result == 0:
    print("x e igual a y")
else:
    print("x e menor que y")