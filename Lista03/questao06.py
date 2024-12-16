n = int(input())

while True:
    chute = int(input())
    if chute < n:
        print("O número correto é maior.")
    elif chute > n:
        print("O número correto é menor.")
    else:
        print("Parabéns! Você acertou.")
        break
