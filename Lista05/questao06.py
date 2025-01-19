def sopa_de_letras(sopa_completa, sopa_restante):
    letras_procuradas = 'JOHN'
    comidas = 0

    for letra in letras_procuradas:
        total_letra = sopa_completa.lower().count(letra.lower())
        nao_comidas = sopa_restante.lower().count(letra.lower())
        comidas += total_letra - nao_comidas

    print(comidas, nao_comidas)