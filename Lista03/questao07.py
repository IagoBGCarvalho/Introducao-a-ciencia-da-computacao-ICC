def fibonacci(n):
    if n == 1 or n == 2:
        return 1, 1  # Retorna o termo atual e o penúltimo termo
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b, a  # b é o termo atual, a é o penúltimo termo

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input())
casais, penultimo_casais = fibonacci(n)
n_fatorial = fatorial(n)

if casais % 2 == 0:
    novos_casais = penultimo_casais
    print(f"{casais} {n_fatorial} {novos_casais}")
else:
    print(f"{casais} {n_fatorial}")
