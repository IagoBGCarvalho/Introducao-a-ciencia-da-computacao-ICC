x = int(input())

horas = x // 3600
minutos = (x % 3600) // 60
segundos = x % 60

print(f"{horas}h:{minutos}m:{segundos}s")