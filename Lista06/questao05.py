n = int(input())

cenario = [input().split() for _ in range(n)]

for coluna in range(n):
    coluna_atual = [cenario[linha][coluna] for linha in range(n)]
    
    blocos_fixos = [x for x in coluna_atual if x == 'x']
    blocos_moveis = [o for o in coluna_atual if o == 'o']
    
    nova_coluna = ['.'] * (n - len(blocos_fixos) - len(blocos_moveis)) + blocos_moveis + blocos_fixos
    
    for linha in range(n):
        cenario[linha][coluna] = nova_coluna[linha]

for linha in cenario:
    print(' '.join(linha))
