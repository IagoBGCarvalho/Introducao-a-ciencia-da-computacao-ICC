# Lendo o número de iterações
N = int(input())

# Armazenando os depósitos em um dicionário
depositos = {}
for _ in range(N):
    S, D = input().split(maxsplit=1)
    depositos[S] = D

# Ordenando os depositantes em ordem alfabética
depositantes_ordenados = sorted(depositos.keys())

# Exibindo o número de depositantes diferentes
J = len(depositantes_ordenados)
print(J)

# Exibindo as marmitas na ordem alfabética dos depositantes
for depositante in depositantes_ordenados:
    print(depositos[depositante])