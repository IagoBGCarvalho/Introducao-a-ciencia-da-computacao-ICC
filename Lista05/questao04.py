def contar_letras(n, linhas):
    cont_p = 0
    cont_u = 0

    for linha in linhas:
        cont_p += linha.lower().count('p')
        cont_u += linha.lower().count('u')
    
    return cont_p, cont_u

n = int(input().strip())
linhas = [input().strip() for _ in range(n)]

resultado_p, resultado_u = contar_letras(n, linhas)

print(resultado_p, resultado_u)