# Dicionário para mapear tags para listas de caminhos
tag_to_paths = {}

# Lendo o número de teorias
N = int(input())

# Processando cada teoria
for _ in range(N):
    parts = input().split()
    path = parts[0]  # Caminho do arquivo
    tags = parts[1:]  # Tags associadas ao arquivo

    # Associando cada tag ao caminho do arquivo
    for tag in tags:
        if tag not in tag_to_paths:
            tag_to_paths[tag] = []
        tag_to_paths[tag].append(path)

# Lendo as tags de pesquisa
search_tags = input().split()

# Buscando os caminhos correspondentes às tags de pesquisa
result_paths = []
for tag in search_tags:
    if tag in tag_to_paths:
        result_paths.extend(tag_to_paths[tag])

# Exibindo os resultados
for path in result_paths:
    print(path)