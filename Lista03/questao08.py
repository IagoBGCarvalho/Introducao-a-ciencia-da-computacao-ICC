numeros = []
while True:
    n = int(input())
    if n == 0:
        break
    numeros.append(n)

if numeros:
    quantidade = len(numeros)
    maior = max(numeros)
    media = sum(numeros) / quantidade
else:
    quantidade = 0
    maior = 0
    media = 0.0

print(quantidade)
print(maior)
print(f"{media:.2f}")
