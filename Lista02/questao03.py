cargo = input()
tempo_servico = int(input())
salario = float(input())

if (salario < 1039.00):
    print("Salário inválido!")
else:
    if (cargo == "Gerente"):
        if (tempo_servico <= 3):
            percentual = 12
        elif ( 3 >= tempo_servico <= 6):
            percentual = 13
        else:
            percentual = 15
    elif (cargo == "Engenheiro"):
        if (tempo_servico <= 3):
            percentual = 7
        elif ( 3 >= tempo_servico <= 6):
            percentual = 11
        else:
            percentual = 14
    else:
        percentual = 5

reajuste = salario * (percentual / 100)
salario_reajustado = salario + reajuste

print(f"{reajuste:.2f}")
print(f"{salario_reajustado:.2f}")