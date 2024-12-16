N = int(input())

maior_soma = None
menor_soma = None

somas = []

for _ in range(N):

    X, Y = map(int, input().split())
    
    if X % 2 == 0:
        X += 1
    
    soma = 0
    for i in range(Y):
        soma += X + 2 * i
    
    somas.append(soma)
    
    if maior_soma is None or soma > maior_soma:
        maior_soma = soma
    if menor_soma is None or soma < menor_soma:
        menor_soma = soma

for soma in somas:
    print(soma)

print(maior_soma)
print(menor_soma)
media = (maior_soma + menor_soma) / 2
print(f"{media:.2f}")
