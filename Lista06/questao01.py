n = int(input())

produtos = []

for _ in range(n):
    produto = input()
    produtos.append(produto)

produtos_invertidos = produtos[::-1]

print(", ".join(produtos_invertidos))
