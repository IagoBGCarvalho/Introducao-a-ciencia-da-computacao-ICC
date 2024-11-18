h_inicial, m_inicial, h_final, m_final = map(int, input().split())

inicio_total = h_inicial * 60 + m_inicial
fim_total = h_final * 60 + m_final

if fim_total <= inicio_total:
    fim_total += 24 * 60

duracao_total = fim_total - inicio_total
horas = duracao_total // 60
minutos = duracao_total % 60

print(f"O jogo durou {horas} hora(s) e {minutos} minuto(s).")