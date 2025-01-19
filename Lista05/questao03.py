def determinar_vencedor(palavra_andreia, palavra_brocado):
    if palavra_andreia.lower() > palavra_brocado.lower():
        return "A"
    else:
        return "B"

entrada = input().strip().split()
palavra_andreia, palavra_brocado = entrada[0], entrada[1]

print(determinar_vencedor(palavra_andreia, palavra_brocado))