lados = sorted([float(input()) for _ in range(3)], reverse=True)
A, B, C = lados

if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif A**2 == B**2 + C**2:
    print("TRIANGULO RETANGULO")
elif A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
    print("TRIANGULO ISOSCELES")
else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")
