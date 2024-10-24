deposito = float(input())
juros = float(input())

rendimento = ((deposito * juros) / 100) 
valor_total = deposito + rendimento

print(f"{rendimento:.2f}\n{valor_total:.2f}")