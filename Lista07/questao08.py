import re
from collections import defaultdict

# Lendo a obra
obra = input()

# Removendo pontuação e convertendo para minúsculas
palavras = re.findall(r'\b\w+\b', obra.lower())

# Contando a frequência das palavras
frequencia = defaultdict(int)
for palavra in palavras:
    frequencia[palavra] += 1

# Ordenando as palavras
palavras_ordenadas = sorted(frequencia.items(), key=lambda x: (-x[1], x[0]), reverse=True)

# Exibindo os resultados
for palavra, qtd in palavras_ordenadas:
    print(palavra.capitalize(), qtd)