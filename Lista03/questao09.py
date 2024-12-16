import math

n, m = map(int, input().split())

tamanho_max_pilha = math.gcd(n, m)

print(tamanho_max_pilha)
