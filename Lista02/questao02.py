valor_compra, parcelas = input().split()
valor_compra = float(valor_compra)
parcelas = int(parcelas)

if (parcelas == 1):
    valor_final = valor_compra * 0.95
elif (parcelas == 2):
    valor_final = valor_compra
elif (parcelas == 3):
    valor_final = valor_compra * 1.05
elif (parcelas == 4):
    valor_final = valor_compra * 1.10

prestacoes = (valor_final / parcelas)

print(f"{valor_final:.2f} {prestacoes:.2f}")