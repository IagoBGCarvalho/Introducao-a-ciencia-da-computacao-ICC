m, d = map(int, input().split())

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dias_mes = dias_por_mes[m - 1]

dias_primeira_semana = 8 - d
dias_restantes = dias_mes - dias_primeira_semana
colunas = 1 + (dias_restantes + 6) // 7

print(colunas)
