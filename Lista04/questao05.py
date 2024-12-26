def soma_pares_recursiva(n):
    if n < 0:
        return -1
    if n < 2:
        return 0
    return (n - 2) + soma_pares_recursiva(n - 2) if (n - 2) % 2 == 0 else soma_pares_recursiva(n - 1)

n = int(input())
resultado = soma_pares_recursiva(n)
print(resultado)