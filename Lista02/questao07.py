peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Baixo peso"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso normal"
elif 24.9 < imc <= 29.9:
    classificacao = "Sobrepeso"
elif 29.9 < imc <= 34.9:
    classificacao = "Obesidade grau I"
elif 34.9 < imc <= 39.9:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"

print(f"{imc:.2f}")
print(classificacao)

if imc > 24.9:
    peso_ideal = 24.9 * (altura ** 2)
    peso_a_perder = peso - peso_ideal
    print(f"{peso_a_perder:.2f}")
