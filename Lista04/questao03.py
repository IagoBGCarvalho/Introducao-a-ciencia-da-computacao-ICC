def pares_intervalo(n):
    if n < 2:
        return
    if n % 2 == 0:
        print(n)
    pares_intervalo(n - 1)

n = int(input())
pares_intervalo(n)