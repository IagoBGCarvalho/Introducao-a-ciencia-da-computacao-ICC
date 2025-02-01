# Inicializando as variáveis para cada direção
norte = 0
sul = 0
leste = 0
oeste = 0

# Lendo o número de movimentos
M = int(input())

# Processando cada movimento
for _ in range(M):
    direcao, quantidade = input().split()
    quantidade = int(quantidade)
    
    if direcao == 'N':
        norte += quantidade
    elif direcao == 'S':
        sul += quantidade
    elif direcao == 'L':
        leste += quantidade
    elif direcao == 'O':
        oeste += quantidade

# Calculando o deslocamento necessário para retornar à origem
deslocamento_norte_sul = norte - sul
deslocamento_leste_oeste = leste - oeste

# Determinando a direção final do deslocamento
if deslocamento_norte_sul > 0:
    norte_final = 0
    sul_final = deslocamento_norte_sul
else:
    norte_final = -deslocamento_norte_sul
    sul_final = 0

if deslocamento_leste_oeste > 0:
    leste_final = 0
    oeste_final = deslocamento_leste_oeste
else:
    leste_final = -deslocamento_leste_oeste
    oeste_final = 0

# Exibindo o resultado
print(norte_final, sul_final, leste_final, oeste_final)