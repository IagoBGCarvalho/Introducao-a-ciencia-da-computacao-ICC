nome = input("Digite um nome ou digite 'fim' para encerrar:")
quantidade = 0

while (nome != "fim" or nome != "FIM" or nome != "Fim"):
    quantidade = (quantidade + 1)
    nome = input("Digite um nome ou digite 'fim' para encerrar:")

print(f"Quantidade de nomes: {quantidade}")