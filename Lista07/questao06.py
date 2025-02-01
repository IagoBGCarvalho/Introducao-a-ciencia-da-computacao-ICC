# Lendo o número de palavras críticas
N = int(input())

# Armazenando as palavras críticas e as personalidades em um dicionário
palavras_criticas = {}
for _ in range(N):
    T, P = input().split()
    palavras_criticas[T] = P

# Lendo a frase
frase = input().split()

# Verificando a frase e coletando as personalidades
personalidades = []
for palavra in frase:
    if palavra in palavras_criticas:
        personalidades.append(palavras_criticas[palavra])

# Exibindo o resultado
if personalidades:
    print(" ".join(personalidades))
else:
    print("Tudo bem!")