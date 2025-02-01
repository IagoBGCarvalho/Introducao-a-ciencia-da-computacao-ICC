# Lendo o número de filósofos
F = int(input())

# Armazenando os filósofos em um dicionário
filósofos = {}
for _ in range(F):
    TF, N = input().split(maxsplit=1)
    TF = int(TF)
    filósofos[TF] = N

# Armazenando as lutas em um dicionário
lutas = {}
while True:
    linha = input().split()
    if linha[0] == 'FINISHHIM':
        luta_final = int(linha[1])
        break
    TL, TF1, TF2, TV = map(int, linha)
    lutas[TL] = (TF1, TF2, TV)

# Função para contar o número de lutas até a vitória
def contar_lutas(luta_id):
    if luta_id in filósofos:
        return 0  # Chegamos a um filósofo, não há mais lutas
    TF1, TF2, TV = lutas[luta_id]
    if TV == TF1:
        return 1 + contar_lutas(TF1)
    else:
        return 1 + contar_lutas(TF2)

# Contando o número de lutas até a vitória final
num_lutas = contar_lutas(luta_final)

# Exibindo o resultado
print(num_lutas)