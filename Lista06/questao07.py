def mover(n, origem, aux, destino, passos):
    if n > 0 and passos[0] > 0:
        mover(n - 1, origem, destino, aux, passos)
   
        if passos[0] > 0:
            passos[0] -= 1
            disk = origem[0].pop() 
            destino[0].append(disk) 
        
        mover(n - 1, aux, origem, destino, passos)

h, p = map(int, input().split()) 

pino_original = (list(range(h, 0, -1)), "origem")
pino_auxiliar = ([], "auxiliar")  
pino_destino = ([], "destino")  

mover(h, pino_original, pino_auxiliar, pino_destino, [p])

print(len(pino_original[0]), len(pino_auxiliar[0]), len(pino_destino[0]))
