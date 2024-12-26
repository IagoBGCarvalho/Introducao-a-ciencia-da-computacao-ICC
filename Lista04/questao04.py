def quadrado_pares(n):
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print(f"{i}^2 = {i**2}")

while True:
    n = int(input())
    if n == 0:
        break
    quadrado_pares(n)