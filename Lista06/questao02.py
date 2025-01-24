c = int(input())

convidados = []

for _ in range(c):
    nome = input()
    convidados.append(nome)

if "André" in convidados:
    print("Cuidado!")
else:
    print("Seguro!")
