# Dicionário para armazenar os valores já calculados
computed = {}

def Fack(x, y):
    # Verifica se o valor já foi calculado
    if (x, y) in computed:
        return computed[(x, y)]
    
    # Casos base da função de Ackermann
    if x == 0:
        result = y + 1
    elif x == 1:
        result = y + 2
    elif x == 2:
        result = 2 * y + 3
    elif y == 0:
        result = Fack(x - 1, 1)
    else:
        result = Fack(x - 1, Fack(x, y - 1))
    
    # Armazena o resultado no dicionário
    computed[(x, y)] = result
    return result

# Lendo os valores de x e y
x, y = map(int, input().split())

# Calculando e exibindo o resultado
print(Fack(x, y))