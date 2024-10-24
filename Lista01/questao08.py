x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
z = complex(input().strip())

distancia_entre_pontos = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

modulo = abs(z)

print(f"{distancia_entre_pontos:.4f}")
print(f"{modulo:.4f}")
