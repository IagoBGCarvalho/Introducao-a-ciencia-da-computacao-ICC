cargo = input().strip()
tempo_servico = int(input())
salario_atual = float(input())

if salario_atual < 1039.00:
    print("Salário inválido!")
else:
    if cargo.lower() == "gerente":
        if tempo_servico <= 3:
            percentual_reajuste = 12
        elif 3 < tempo_servico <= 6:
            percentual_reajuste = 13
        else:
            percentual_reajuste = 15
    elif cargo.lower() == "engenheiro":
        if tempo_servico <= 3:
            percentual_reajuste = 7
        elif 3 < tempo_servico <= 6:
            percentual_reajuste = 11
        else:
            percentual_reajuste = 14
    else:
        percentual_reajuste = 5

    reajuste = salario_atual * (percentual_reajuste / 100)
    salario_reajustado = salario_atual + reajuste

    print(f"{reajuste:.2f}")
    print(f"{salario_reajustado:.2f}")