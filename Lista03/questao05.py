n = int(input())
bacias = [input().split() for _ in range(n)]

maior_pluv_anual = ""
maior_pluv_valor = 0
menor_pluv_estacao = ""
menor_pluv_valor = float("inf")
area_total = 0

for bacia in bacias:
    nome = " ".join(bacia[:-5])
    area = float(bacia[-5])
    pluverao = float(bacia[-4])
    pluoutono = float(bacia[-3])
    pluiverno = float(bacia[-2])
    plusprimavera = float(bacia[-1])

    pluv_total = pluverao + pluoutono + pluiverno + plusprimavera
    menor_pluv_local = min(pluverao, pluoutono, pluiverno, plusprimavera)

    if pluv_total > maior_pluv_valor:
        maior_pluv_valor = pluv_total
        maior_pluv_anual = nome

    if menor_pluv_local < menor_pluv_valor:
        menor_pluv_valor = menor_pluv_local
        menor_pluv_estacao = nome

    area_total += area

area_media = area_total / n

print(maior_pluv_anual)
print(menor_pluv_estacao)
print(f"{area_media:.2f}")
