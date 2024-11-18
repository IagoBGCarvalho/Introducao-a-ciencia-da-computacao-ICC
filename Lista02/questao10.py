t1, v1, t2, v2 = map(int, input().split())

ideal_t1 = 30 * 60
ideal_t2 = 60 * 60
limite_v1 = 60
limite_v2 = 40

if t1 == 0:
    pontos_t1_sem_vel = -1000
else:
    if t1 > ideal_t1:
        pontos_t1_sem_vel = -(t1 - ideal_t1)
    else:
        pontos_t1_sem_vel = -(ideal_t1 - t1) * 2

if t1 == 0:
    pontos_t1_com_vel = -1000
else:
    excesso_v1 = max(0, v1 - limite_v1) * 10
    pontos_t1_com_vel = pontos_t1_sem_vel - excesso_v1

if t2 == 0:
    pontos_t2_sem_vel = -1000
else:
    if t2 > ideal_t2:
        pontos_t2_sem_vel = -(t2 - ideal_t2)
    else:
        pontos_t2_sem_vel = -(ideal_t2 - t2) * 2

if t2 == 0:
    pontos_t2_com_vel = -1000
else:
    excesso_v2 = max(0, v2 - limite_v2) * 20
    pontos_t2_com_vel = pontos_t2_sem_vel - excesso_v2

pontos_totais_sem_vel = pontos_t1_sem_vel + pontos_t2_sem_vel
pontos_totais_com_vel = pontos_t1_com_vel + pontos_t2_com_vel

print(pontos_t1_sem_vel)
print(pontos_t1_com_vel)
print(pontos_t2_sem_vel)
print(pontos_t2_com_vel)
print(pontos_totais_sem_vel)
print(pontos_totais_com_vel)
