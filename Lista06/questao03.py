f, p = map(int, input().split())

fatiado = list(range(f))

for _ in range(f):
    nome, indice = input().split()
    indice = int(indice)
    
    if fatiado[indice] == p:
        print(nome)
        break

    fatiado.pop(indice)
