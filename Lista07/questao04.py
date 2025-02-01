# Lendo o número de jogadas
N = int(input())

# Armazenando as jogadas em uma lista
jogadas = []
for _ in range(N):
    J, I = input().split()
    I = int(I)
    jogadas.append((J, I))

# Iniciando a simulação do jogo
posicao_atual = N  # Começamos pela última jogada
visitados = set()  # Conjunto para armazenar as posições já visitadas

while True:
    if posicao_atual in visitados:
        # Encontramos uma repetição, o vencedor é o jogador dessa posição
        vencedor = jogadas[posicao_atual - 1][0]
        break
    visitados.add(posicao_atual)
    posicao_atual = jogadas[posicao_atual - 1][1]  # Movemos para a próxima posição

    # Se a posição atual for inválida (fora do intervalo), o vencedor é o último jogador
    if posicao_atual < 1 or posicao_atual > N:
        vencedor = jogadas[-1][0]
        break

# Exibindo o vencedor
print(vencedor)