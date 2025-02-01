# Lendo o número de atividades
N = int(input())

# Armazenando as atividades
atividades = []
for _ in range(N):
    linha = input().split()
    # O título da atividade pode conter espaços, então juntamos todas as partes, exceto as duas últimas (horários)
    T = ' '.join(linha[:-2])  # Título da atividade
    C = linha[-2]  # Horário de início
    F = linha[-1]  # Horário de término
    atividades.append((T, C, F))

# Função para converter horário em minutos
def horario_para_minutos(horario):
    hh, mm = map(int, horario.split(':'))
    return hh * 60 + mm

# Ordenando as atividades pelo horário de término
atividades_ordenadas = sorted(atividades, key=lambda x: horario_para_minutos(x[2]))

# Selecionando as atividades
selecionadas = []
ultimo_fim = 0
for atividade in atividades_ordenadas:
    inicio = horario_para_minutos(atividade[1])
    fim = horario_para_minutos(atividade[2])
    if inicio >= ultimo_fim:
        selecionadas.append(atividade[0])
        ultimo_fim = fim

# Exibindo os resultados
M = len(selecionadas)
print(M)
if M > 0:
    for atividade in selecionadas:
        print(atividade)