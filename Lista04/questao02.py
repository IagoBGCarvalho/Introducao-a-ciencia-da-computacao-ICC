def ler_numeros():
    numeros = []
    for _ in range(10):
        numeros.append(int(input()))
    return numeros

numeros = ler_numeros()
primeiro = numeros[0]
maior = max(numeros)

print(maior)
if maior % primeiro == 0:
    print(primeiro)
