n = int(input())

prateleira_inicial = input().split()

prateleira_final = prateleira_inicial[:]

for _ in range(3):
    b, m, q = input().split()
    q = int(q)
    
    index = prateleira_final.index(b)
    
    if m == 'DIR':
        novo_index = min(index + q, n - 1)  
    elif m == 'ESQ':
        novo_index = max(index - q, 0)     
  
    prateleira_final.pop(index)
   
    prateleira_final.insert(novo_index, b)

fora_do_lugar = sum(1 for i in range(n) if prateleira_inicial[i] != prateleira_final[i])

print(fora_do_lugar)
