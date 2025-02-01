n = int(input())
problemas = []

for _ in range(n):
    p, s, d = input().split()
    d = int(d)
    problemas.append((d, s))  # Armazena a dificuldade e a solução

# Ordena os problemas por dificuldade de forma decrescente, mantendo a ordem original em caso de empate
problemas.sort(key=lambda x: -x[0])

# Concatena as soluções na ordem correta
resultado = "".join(s for _, s in problemas)
print(resultado)