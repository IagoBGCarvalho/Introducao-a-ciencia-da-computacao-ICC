n = int(input())
notas_faltas = [list(map(float, input().split())) for _ in range(n)]

media_turma = 0
alunos_aprovados = 0

for notas in notas_faltas:
    nota1, nota2, faltas = notas
    media = (nota1 + nota2) / 2
    media_turma += media
    if media >= 5 and faltas <= 20:
        status = "Aprovado"
        alunos_aprovados += 1
    elif 3 < media < 5 and faltas <= 20:
        status = "Exame"
    else:
        status = "Reprovado"
    print(f"{media:.1f} {status}")

media_turma /= n
print(f"{media_turma:.1f} {alunos_aprovados}")
